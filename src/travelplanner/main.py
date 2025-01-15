#!/usr/bin/env python
import sys
import warnings

from travelplanner.crew import MyProject
from mem0 import MemoryClient

client = MemoryClient()

import logging

# Disable OpenTelemetry warnings
logging.getLogger('opentelemetry').setLevel(logging.ERROR)

from travelplanner.crew import MyProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
warnings.filterwarnings("ignore", message=".*TracerProvider.*")
warnings.filterwarnings("ignore", message="Overriding of current TracerProvider is not allowed")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew in an interactive chat loop.
    The loop continues until the user types 'exit' or 'quit'.
    """
    history = []
    
    print("Welcome to the chat! Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("\nGoodbye!")
            break
            
        if not user_input:  # Skip empty inputs
            continue

        chat_history = "\n".join(history)
            
        inputs = {
            'user_message': user_input,
            'history': chat_history,
            'topic': user_input  # Adding this for the research task
        }
        response = MyProject().crew().kickoff(inputs=inputs)

        history.append(f"User: {user_input}")
        history.append(f"Assistant: {response}")
        client.add(user_input, user_id="User")

        print(f"Assistant: {response}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "input": "AI LLMs"
    }
    try:
        MyProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "input": "AI LLMs"
    }
    try:
        MyProject().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
