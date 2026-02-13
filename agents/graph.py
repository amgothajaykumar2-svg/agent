from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import AgentState
from agents import researcher_agent, writer_agent
from langchain_core.messages import HumanMessage

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("Researcher", researcher_agent)
workflow.add_node("Writer", writer_agent)

# Define entry point
workflow.set_entry_point("Researcher")

# Define edges
# Simple flow: Researcher -> Writer -> END
# In a real multi-agent system, we'd have a router invoked here to decide next steps.
# For this demo of memory, we'll keep the flow linear but allow it to be re-triggered.
workflow.add_edge("Researcher", "Writer")
workflow.add_edge("Writer", END)

# Initialize memory
memory = MemorySaver()

# Compile the graph with memory
graph = workflow.compile(checkpointer=memory)
