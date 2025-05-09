#!/bin/bash

# Démarrer Streamlit en arrière-plan
streamlit run app_crewai.py --server.port 8501 --server.address 0.0.0.0 &
STREAMLIT_PID=$!

# Simuler une requête HTTP pour signaler que l'app a démarré
sleep 10
curl -s http://localhost:8501/_stcore/health

# Maintenir le conteneur actif
wait $STREAMLIT_PID
