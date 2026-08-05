#!/usr/bin/env python3
"""Compara o pacote packwiz com a pasta de mods real e aponta divergências.

Uso: python3 scripts/auditar.py [caminho-da-pasta-mods]
"""

import re
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
PADRAO_MODS = Path("/home/sacer/.minecraft/modpacks/Modpack/mods")


def nomes_no_pacote() -> set[str]:
    """Nomes de jar cobertos pelo pacote: metadados + jars embutidos."""
    nomes = {jar.name for jar in (PACK / "mods").glob("*.jar")}
    for meta in (PACK / "mods").glob("*.pw.toml"):
        achado = re.search(r'filename\s*=\s*"(.*?)"', meta.read_text(encoding="utf-8"))
        if achado:
            nomes.add(achado.group(1))
    return nomes


def main() -> int:
    mods_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else PADRAO_MODS
    if not mods_dir.is_dir():
        print(f"ERRO: pasta não encontrada: {mods_dir}")
        return 2

    reais = {jar.name for jar in mods_dir.glob("*.jar")}
    pacote = nomes_no_pacote()

    faltando = sorted(reais - pacote)
    sobrando = sorted(pacote - reais)

    print(f"Pasta real: {len(reais)} jars")
    print(f"Pacote:     {len(pacote)} entradas")
    print(f"Cobertos:   {len(reais & pacote)}\n")

    for nome in faltando:
        print(f"  FALTA no pacote: {nome}")
    for nome in sobrando:
        print(f"  SOBRA no pacote: {nome}")

    if not faltando and not sobrando:
        print("Tudo certo — pacote e pasta batem exatamente.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
