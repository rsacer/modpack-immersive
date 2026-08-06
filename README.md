# Modpack — 1.20.1 / Forge 47.4.22 / Java 17

136 mods. Aqui ficam só os metadados; os jars são baixados na instalação.

## Instalar

Na pasta da instância (onde ficam `mods/` e `config/`):

1. **Apague a pasta `mods/`** se você já tinha o pack pelo zip antigo.
2. Baixe o [packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest).
3. Crie um `atualizar.bat` e rode:

```bat
@echo off
cd /d "%~dp0"
java -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/rsacer/modpack-immersive/main/pack.toml
pause
```

No Prism Launcher, em vez do `.bat`, cole a linha do `java -jar` em
Settings → Custom commands → Pre-launch command. Aí atualiza sozinho.

## Atualizar

Rode o `atualizar.bat` de novo. Baixa só o que mudou.

## Mantenedor

```bash
packwiz modrinth add <slug>        # ou: packwiz curseforge add / remove / update --all
python3 scripts/auditar.py         # confere se bate com ../Modpack/mods/
packwiz refresh && git add -A && git commit -m "..." && git push
```

Cuidado com `-y` no add: ele aceita dependências opcionais sozinho e já
trouxe mod indesejado pro pack.
