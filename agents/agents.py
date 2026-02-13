import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import get_search_tool

# Ensure environment variables are loaded if this file is imported elsewhere
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini with explicit API key from environment
if not google_api_key:
    print("Error: GOOGLE_API_KEY not found in environment variables.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=google_api_key,
    temperature=0
)

# --- Researcher Agent ---
# The new create_agent returns a compiled graph that can be used as a node.
researcher_agent = create_agent(
    model=llm,
    tools=[get_search_tool()],
    system_prompt="You are a web researcher. You search for detailed information based on the user's request. "
                  "Provide comprehensive and accurate findings.",
    name="Researcher"
)

# --- Writer Agent ---
writer_agent = create_agent(
    model=llm,
    tools=[], # Writer doesn't need tools, just writes based on conversation history
    system_prompt="You are a professional writer. You summarize and synthesize information provided by the Researcher. "
                  "Create a well-structured and engaging final answer for the user.",
    name="Writer"
)

