from langchain_tavily import TavilySearch
import os

def get_search_tool():
    """Returns the modern Tavily search tool."""
    # Ensure API key is set
    if not os.environ.get("TAVILY_API_KEY"):
        print("Warning: TAVILY_API_KEY not found in environment. Search may fail.")
    
    return TavilySearch(max_results=2)
