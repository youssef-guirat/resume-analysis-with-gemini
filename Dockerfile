# Utiliser la même version que ton environnement local
FROM python:3.11.9-slim

# Créer et définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
