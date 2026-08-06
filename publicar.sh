#!/bin/bash
# Publica o estado atual do modpack para os jogadores.
# Uso: ./publicar.sh "descrição da mudança"
set -e
cd "$(dirname "$0")"

MSG="${1:-Atualização do modpack}"

echo "== Conferindo se o catálogo bate com a pasta de mods =="
if ! python3 scripts/auditar.py; then
    echo
    echo "DIVERGÊNCIA: há mod na pasta que não está no catálogo (ou vice-versa)."
    echo "Peça ao CTO para sincronizar antes de publicar."
    exit 1
fi

echo
echo "== Reindexando =="
/home/sacer/.local/bin/packwiz refresh

echo
echo "== Publicando =="
git add -A
if git diff --cached --quiet; then
    echo "Nada mudou desde a última publicação."
    exit 0
fi
git commit -m "$MSG"
git push origin main
echo
echo "Publicado. Avise os jogadores para rodarem o atualizar.bat."
