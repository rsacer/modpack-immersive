# Modpack — Minecraft 1.20.1 / Forge 47.4.22

Modpack com Immersive Engineering como eixo central: indústria, exploração,
sobrevivência com estações e temperatura, criaturas e magia.

**136 mods.** O repositório guarda apenas os metadados (~4 MB); os jars são
baixados das fontes oficiais na instalação.

---

## Para os jogadores

### Requisitos

- **Minecraft 1.20.1** com **Forge 47.4.22** (exatamente essa versão)
- **Java 17** — o Forge 1.20.1 é feito para ele. Java 21 ou 25 causam
  Metaspace inflado e crashes difíceis de diagnosticar.
- **6 GB de RAM** alocados (`-Xmx6G`) para 16 GB de RAM física. Não aumente
  além disso: heap grande deixa o coletor de lixo preguiçoso.

### Instalação

**1.** Baixe o [packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest)
e coloque na **pasta da instância** — a mesma onde ficam `mods/`, `config/`
e `options.txt`.

**2.** Rode o instalador. O jeito depende do launcher:

**Prism Launcher / MultiMC / ATLauncher** — em `Editar instância → Settings →
Custom commands`, marque a opção e cole em **Pre-launch command**:

```
java -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/rsacer/modpack-immersive/main/pack.toml
```

A partir daí **abrir o jogo já atualiza** o pack. Não há mais nada a fazer.

**SKLauncher / launcher oficial** — não têm campo de pre-launch. Crie um
arquivo `atualizar.bat` na pasta da instância com este conteúdo:

```bat
@echo off
cd /d "%~dp0"
java -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/rsacer/modpack-immersive/main/pack.toml
pause
```

Dois cliques nele sempre que o pack for atualizado, antes de abrir o jogo.

> O `cd /d "%~dp0"` garante que o comando roda na pasta certa mesmo se você
> executar de outro lugar. O `pause` mantém a janela aberta para você ler a
> saída.

### Atualizar

O instalador compara os hashes e **baixa só o que mudou** — trocar três mods
custa alguns MB, não os 500 MB do pacote inteiro. No Prism é automático; nos
outros launchers, rode o `atualizar.bat`.

---

## Migrando de uma instalação antiga (.zip)

Se você recebeu o pack como `.zip` antes do repositório existir:

**1. Apague a pasta `mods/` inteira.** Isso não é opcional — o zip antigo tem
mods que já foram removidos do pack (Immersive Railroading, UniversalModCore,
TrackAPI, betterchunkloading). O instalador não apaga sobras, e um jar a mais
faz o Forge recusar a conexão por divergência de lista de mods.

**2. Mantenha a pasta `config/`.** As configs do pack são sobrescritas pelas
versões corretas; suas configs locais de vídeo permanecem intactas.

**3.** Siga a instalação normal acima.

### Configurações que são suas, não do pack

Estes arquivos **não** vêm do repositório — cada máquina mantém os seus:

| Arquivo | O que é |
|---|---|
| `config/embeddium-options.json` | Threads de chunk builder, qualidade de render |
| `config/oculus.properties` | Shader ativo e suas opções |
| `options.txt` | Teclas, distâncias de render/simulação, volume |

Ajuste uma vez e eles nunca serão sobrescritos por uma atualização.

---

## Solução de problemas

**`ClassNotFoundException: packwiz-installer-bootstrap.jar`**
O `-jar` sumiu do comando, ou o nome do arquivo não bate. Confira se há espaço
entre `java` e `-jar`, e rode `dir` para ver o nome real do arquivo baixado —
o navegador pode ter salvo como `packwiz-installer-bootstrap(1).jar` ou, com
extensões ocultas no Windows, como `.jar.txt`.

**O jogo abre mas o amigo não consegue conectar**
Lista de mods divergente. Os dois lados precisam do mesmo conjunto: rode o
instalador em ambos e confira se ninguém tem jar sobrando em `mods/`.

**Crash ou travamento sem causa aparente**
Confirme a versão do Java com `java -version`. Precisa ser 17.

---

## Para o mantenedor

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
> com o script de auditoria.

### Publicar uma alteração

```bash
packwiz refresh
python3 scripts/auditar.py      # confere se o pacote bate com ../Modpack/mods/
git add -A
git commit -m "descrição da mudança"
git push
```

Avise os jogadores para rodarem o instalador.

---

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `pack.toml` | Metadados: nome, versão, Minecraft e Forge |
| `index.toml` | Índice com hash de cada arquivo |
| `mods/*.pw.toml` | Um metadado por mod (origem, versão, hash) |
| `mods/*.jar` | Mods sem fonte automática, embutidos |
| `config/` | Configurações compartilhadas do pack |
| `scripts/auditar.py` | Compara o pacote com a pasta de mods real |

### Mod embutido

`morevillagers` não resolve por slug automático, então vai como jar dentro
do repositório — a licença dele é MIT, que permite redistribuição.

> **Antes de embutir qualquer jar,** confira a licença:
> `unzip -p <arquivo>.jar META-INF/mods.toml | grep license`.
> Mods marcados como `ARR` (*All Rights Reserved*) não podem ser
> redistribuídos — referencie-os pela fonte oficial.
