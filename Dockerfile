# Image Ubuntu officielle
FROM ubuntu:22.04

# Mettre à jour le système et installer Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common \
        ca-certificates && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update

# Installer Python 3.9 et les dépendances système
RUN apt-get install -y --no-install-recommends \
        python3.9 \
        python3-pip \
        build-essential \
        gcc \
        g++ \
        libgl1 \
        libsm6 \
        libxrender1 \
        libxext6 \
        ffmpeg \
        && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Créer un lien symbolique pour python
RUN ln -s /usr/bin/python3.9 /usr/bin/python

# Installer pip et setuptools
RUN curl https://bootstrap.pypa.io/get-pip.py  -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Répertoire de travail
WORKDIR /app

# Copie des fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app_crewai.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
