from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class DuckDuckGoSearchInput(BaseModel):
    """Input schema for DuckDuckGoSearchTool."""
    query: str = Field(..., description="The search query string.")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGoSearch"
    description: str = (
        "A tool to perform web searches using DuckDuckGo. "
        "Useful for finding information on various topics."
    )
    args_schema: Type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> str:
        response = requests.get(
            "https://api.duckduckgo.com/",
            params={
                "q": query,
                "format": "json",
                "no_html": 1,
                "skip_disambig": 1
            }
        )
        data = response.json()
        abstract = data.get("Abstract", "No abstract available.")
        return abstract

    def _arun(self, query: str):
        raise NotImplementedError("DuckDuckGoSearchTool does not support async")