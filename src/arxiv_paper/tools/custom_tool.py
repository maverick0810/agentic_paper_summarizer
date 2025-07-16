from typing import Type, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import arxiv
import os
import requests
import fitz

class ResearchToolInput(BaseModel):
    """Input schema for ResearchTool."""
    query: str = Field(..., description="query to search arXiv for")
    max_results: int = Field(1, description='Number of articles to fetch')

class ResearchTool(BaseTool):
    name: str = "ResearchTool"
    description: str = (
        'Given the query, it fetches the relevant arXiv papers and downloads them'
    )
    args_schema: Type[BaseModel] = ResearchToolInput

    def _run(self, query: str, max_results: int) -> list:
        arxiv_paper_dir = "arxiv_papers"
        os.makedirs(arxiv_paper_dir, exist_ok=True)
        search = arxiv.Search(
            query=query,
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
        papers = []
        for result in search.results():
            print(f"Found: {result.title}")
            try:
                pdf_url = result.pdf_url
                paper_id = result.entry_id.split('/')[-1]
                pdf_filename = os.path.join(arxiv_paper_dir, f"{paper_id}.pdf")
                response = requests.get(pdf_url)
                response.raise_for_status()
                with open(pdf_filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {pdf_filename}")
                papers.append(pdf_filename)
            except Exception as e:
                print(f"Failed to download {result.title}: {e}")
        return papers

class TextExtractorInput(BaseModel):
    """Input schema for ResearchTool."""
    file_paths: List[str] = Field(..., description="List of file paths to extract text from")

class TextExtractorTool(BaseTool):
    name: str = "TextExtractorTool"
    description: str = (
        'Given the query, it fetches the relevant arXiv papers and downloads them'
    )
    args_schema: Type[BaseModel] = TextExtractorInput
    
    def _run(self, file_paths: List[str]) -> str:
        if not file_paths:  # Empty list
            return ""
        first_path = file_paths[0]
        if not os.path.exists(first_path):
            return ""
        try:
            all_text = ""
            doc = fitz.open(first_path)
            for page in doc:
                page_text = page.get_text()
                if page_text:
                    all_text += page_text + "\n"
            return all_text
        except Exception as e:
            # Optionally, log error here
            return ""