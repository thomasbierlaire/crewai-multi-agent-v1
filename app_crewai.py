import os

# Force EMBEDCHAIN_HOME avant tout import de crewai
os.environ["EMBEDCHAIN_HOME"] = "/tmp/.embedchain"
os.makedirs("/tmp/.embedchain", exist_ok=True)

import streamlit as st

st.write("✅ Application en cours de démarrage...")

from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

st.set_page_config(page_title="Agent Multi-Crew IA", layout="centered")

st.title("🧠 Système Multi-Agents - Crew AI")
topic = st.text_input("Entrez le sujet à traiter", "Énergie renouvelable en 2024")

if st.button("Générer l'article"):
    with st.spinner("Recherche et rédaction en cours..."):

        # Outilss
        search_tool = DuckDuckGoSearchRun()

        # Agents
        researcher = Agent(
            role='Research Specialist',
            goal='Find accurate and up-to-date information on a given topic.',
            backstory="You are an expert researcher who knows how to find reliable sources quickly.",
            verbose=True,
            tools=[search_tool]
        )

        writer = Agent(
            role='Content Writer',
            goal='Write clear, engaging, and well-structured articles based on research.',
            backstory="You are a skilled writer who can turn complex information into easy-to-understand content.",
            verbose=True
        )

        # Tâches
        task_research = Task(
            description=f"Research the latest trends in {topic} for 2024.",
            agent=researcher
        )

        task_write = Task(
            description=f"Write a 500-word article summarizing the findings from the research task on {topic}.",
            agent=writer
        )

        # Équipe
        crew = Crew(
            agents=[researcher, writer],
            tasks=[task_research, task_write],
            process=Process.sequential,
            memory=False
        )

        result = crew.kickoff()
        st.success("Article généré !")
        st.markdown(result)
