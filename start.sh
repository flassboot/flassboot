#!/bin/bash

echo "Pornesc aplicația Flask și botul..."

# Verifică dacă folderul venv există
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Eroare: Folderul venv nu există. Instalează dependințele cu 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'"
    exit 1
fi

# Rulează aplicația
python app.py
