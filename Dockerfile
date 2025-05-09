# Utilise une image Ubuntu avec Python déjà disponible
FROM ubuntu:22.04

# Mettre à jour et installer les outils de base
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        ffmpeg \
        libgl1 \
        libsm6 \
        libxrender1 \
        libxext6 \
        git \
        curl \
        && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Créer un lien symbolique python → python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Installer pip si nécessaire
RUN curl https://bootstrap.pypa.io/get-pip.py  -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Répertoire de travail
WORKDIR /app

# Copie des fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiez et rendez exécutable le script de démarrage
RUN chmod +x /start.sh

EXPOSE 8501

CMD ["streamlit", "run", "app_crewai.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
