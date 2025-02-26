#!/bin/bash

echo "🚀 Pornesc aplicația Flask..."

# Verifică dacă folderul venv există
if [ -d "venv" ]; then
    source venv/bin/activate  # Linux/Mac
    # Pentru Windows (dacă rulezi cu Git Bash sau WSL)
    # source venv/Scripts/activate
else
    echo "❌ Eroare: Folderul 'venv' nu există. Rulează: python3 -m venv venv"
    exit 1
fi

# Instalează dependințele dacă nu sunt instalate
pip install -r requirements.txt

# Rulează aplicația
python3 app.py
