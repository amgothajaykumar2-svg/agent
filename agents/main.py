import os
from dotenv import load_dotenv

# Load environment variables first!
load_dotenv()

from langchain_core.messages import HumanMessage
from graph import graph

def main():
    print("Initialize Multi-Agent Research System...")
    
    # Check for API keys
    if not os.getenv("GOOGLE_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        print("Error: GOOGLE_API_KEY and TAVILY_API_KEY must be set in .env file.")
        return

    # Initialize a thread ID for memory persistence
    thread_id = input("Enter a thread ID (e.g., 'session_1'): ") or "session_1"
    config = {"configurable": {"thread_id": thread_id}}

    print(f"Starting chat session (Thread ID: {thread_id}). Type 'exit' to quit.")
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # The state input is a dictionary with "messages"
        input_state = {"messages": [HumanMessage(content=user_input)]}
        
        print("\n--- Processing ---")
        # Stream the graph execution
        for event in graph.stream(input_state, config=config):
            for key, value in event.items():
                print(f"\n[{key}]:")
                # value is the state update, which contains "messages"
                if "messages" in value:
                     # Get the last message from the node's output
                    last_msg = value["messages"][-1]
                    print(last_msg.content)
        print("\n--- Done ---")

if __name__ == "__main__":
    main()
