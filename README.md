# Modpack — Minecraft 1.20.1 / Forge 47.4.22

Modpack com Immersive Engineering como eixo central: indústria, exploração,
sobrevivência com estações e temperatura, e civilização via MineColonies.

**119 mods.** O repositório guarda apenas os metadados (~2 MB); os jars são
baixados das fontes oficiais na instalação.

---

## Para os jogadores — instalar e atualizar

### Instalação (uma única vez)

1. Instale o **Minecraft 1.20.1 com Forge 47.4.22**.
2. Baixe o [packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest)
   e coloque na pasta da instância.
3. No launcher, adicione este comando pré-lançamento na instância:

   ```
   java -jar packwiz-installer-bootstrap.jar <URL_DO_PACK>/pack.toml
   ```

Pronto. A partir daí o pack se instala e se mantém atualizado sozinho.

### Atualizar

Não há nada a fazer: **abrir o jogo já atualiza**. O instalador compara os
hashes, baixa só o que mudou e ignora o resto. Trocar três mods costuma custar
alguns MB, não os 500 MB do pacote inteiro.

---

## Para o mantenedor — editar o pack

Todos os comandos rodam nesta pasta.

```bash
packwiz modrinth add <slug>       # adiciona mod do Modrinth
packwiz curseforge add <slug>     # adiciona mod do CurseForge
packwiz remove <slug>             # remove um mod
packwiz update <slug>             # atualiza um mod
packwiz update --all              # atualiza todos
packwiz refresh                   # reindexa após mexer em arquivos na mão
```

> **Atenção ao `-y`:** ele aceita automaticamente todas as dependências
> opcionais sugeridas, o que já trouxe mods indesejados (Quark, Iron Chests)
> para dentro do pack. Prefira responder às perguntas, e confira o resultado
> com o script de auditoria abaixo.

### Publicar uma alteração

```bash
packwiz refresh
git add -A
git commit -m "descrição da mudança"
git push
```

Os jogadores recebem na próxima vez que abrirem o jogo.

### Conferir se o pack bate com a pasta de mods real

```bash
python3 scripts/auditar.py
```

Aponta divergências entre este pacote e `../Modpack/mods/`.

---

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `pack.toml` | Metadados: nome, versão, Minecraft e Forge |
| `index.toml` | Índice com hash de cada arquivo |
| `mods/*.pw.toml` | Um metadado por mod (origem, versão, hash) |
| `mods/*.jar` | Os 2 mods sem fonte automática, embutidos |
| `config/` | Configurações compartilhadas do pack |

### Mod embutido

`morevillagers` não resolve por slug automático, então vai como jar dentro
do repositório — a licença dele é MIT, que permite redistribuição. Ao
atualizá-lo, troque o arquivo e rode `packwiz refresh`.

> **Antes de embutir qualquer jar,** confira a licença do mod:
> `unzip -p <arquivo>.jar META-INF/mods.toml | grep license`.
> Mods marcados como `ARR` (*All Rights Reserved*) não podem ser
> redistribuídos — referencie-os pela fonte oficial com
> `packwiz curseforge add`.
