# Modpack — 1.20.1 / Forge 47.4.22 / Java 17

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

## Atualizar

Rode o `atualizar.bat` de novo. Baixa só o que mudou.
