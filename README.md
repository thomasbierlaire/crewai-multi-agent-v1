# 💡 Système Multi-Agents Crew AI + Streamlit

Template prêt à déployer sur **Hugging Face Spaces** avec intégration automatique via **GitHub Actions**.

## 🛠 Technologies utilisées

- [Streamlit](https://streamlit.io/ )
- [Crew AI](https://github.com/joaomdmoura/crewAI )
- [LangChain Community Tools](https://python.langchain.com/docs/integrations/tools/ )

## ▶️ Lancement local

```bash
docker build -t crewai-app .
docker run -p 8501:8501 crewai-app
