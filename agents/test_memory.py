import asyncio
import os
from dotenv import load_dotenv

# Load environment variables first!
load_dotenv()

from graph import graph
from langchain_core.messages import HumanMessage


async def test_memory():
    # Ensure API keys are present
    if not os.getenv("GOOGLE_API_KEY"):
        print("Skipping test: GOOGLE_API_KEY not found.")
        return

    print("Starting Memory Test...")
    
    # Run 1: Tell the agent my name
    config = {"configurable": {"thread_id": "test_thread_1"}}
    input_1 = {"messages": [HumanMessage(content="Hi, my name is Alice.")]}
    
    print("\n--- Run 1: Introduction ---")
    async for event in graph.astream(input_1, config=config):
        for key, value in event.items():
            if "messages" in value:
                print(f"{key}: {value['messages'][-1].content}")

    # Run 2: Ask the agent my name (new run, same thread_id)
    input_2 = {"messages": [HumanMessage(content="What is my name?")]}
    
    print("\n--- Run 2: Recall ---")
    response_content = ""
    async for event in graph.astream(input_2, config=config):
        for key, value in event.items():
            if "messages" in value:
                msg = value["messages"][-1].content
                print(f"{key}: {msg}")
                response_content = msg
    
    # Verification
    if "Alice" in response_content:
        print("\n✅ TEST PASSED: Memory successfully recalled the name.")
    else:
        print("\n❌ TEST FAILED: Memory did NOT recall the name.")

if __name__ == "__main__":
    asyncio.run(test_memory())
