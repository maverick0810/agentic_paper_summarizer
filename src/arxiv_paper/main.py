from pydantic import BaseModel
from crewai.flow import Flow, start, listen
from crews.arxiv_crew.arxiv_paper_crew import ResearchPaperCrew
from dotenv import load_dotenv
load_dotenv()
class ResearchPaperState(BaseModel):
    query: str = ""
    file_paths: list = []
    text:str=""
    summary:str=""
class ResearchPaperFlow(Flow[ResearchPaperState]):

    @start()
    def fetch_research_paper(self):
        print(f"Searching arXiv for {self.state.query}")
        crew = ResearchPaperCrew()
        result = crew.crew().kickoff(inputs={'query': self.state.query,'file_paths':self.state.file_paths, 'text':self.state.text})
        self.state.file_paths = result.raw if hasattr(result, 'raw') else [str(result)]
        print(f"Research completed. Results: {self.state.file_paths}")

    @listen(fetch_research_paper)
    def extract_research_paper(self):
        print(f"Extracting papers from {self.state.file_paths}")
        crew=ResearchPaperCrew()
        result = crew.crew().kickoff(inputs={'query': self.state.query,'file_paths': self.state.file_paths, 'text':self.state.text})
        self.state.text = result.raw if hasattr(result, 'raw') else result
        print("Text extraction complete.")
    @listen(extract_research_paper)
    def summarize(self):
        print('Summarizing Papers')
        crew=ResearchPaperCrew()
        result = crew.crew().kickoff(inputs={'query': self.state.query,'file_paths': self.state.file_paths, 'text':self.state.text})
        self.state.summary = getattr(result, "raw", str(result))

        print("Summarization complete")

def kickoff():
    flow = ResearchPaperFlow()
    query = 'Large Language Models in HealthCare'
    flow.kickoff(inputs={'query': query})

def plot():
    flow = ResearchPaperFlow()
    flow.plot("arxiv_paper_flow.html") 
    

if __name__ == "__main__":
    kickoff()
