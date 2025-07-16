from crewai.project import CrewBase, agent, crew, task
from crewai import Agent, Crew, Process, Task
from tools.custom_tool import ResearchTool, TextExtractorTool

@CrewBase
class ResearchPaperCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def fetch_paper_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["fetch_paper_agent"],
            tools=[ResearchTool()],
            verbose=True
        )
    @agent
    def extract_text_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["extract_text_agent"],
            tools=[TextExtractorTool()],
            verbose=True
        )
    @agent 
    def summarize_agent(self)-> Agent:
        return Agent(
            config=self.agents_config["summarize_agent"],
        
            verbose=True
        )

    @task
    def fetch_paper_task(self) -> Task:
        return Task(
            config=self.tasks_config["fetch_paper_task"]
        )
    @task
    def extract_text_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_text_task"]
        )
    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarize_task"]
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
