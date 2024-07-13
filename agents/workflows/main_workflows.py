from langgraph import Graph, Node
import openai
import re
import httpx
import os
from dotenv import load_dotenv

_ = load_dotenv()
from openai import OpenAI

from langgraph import Graph, Node

# Define nodes for each agent
workout_planner = Node(name="Workout Planner")
nutrition_advisor = Node(name="Nutrition Advisor")
progress_tracker = Node(name="Progress Tracker")

# Create a graph and add nodes
graph = Graph()
graph.add_node(workout_planner)
graph.add_node(nutrition_advisor)
graph.add_node(progress_tracker)

# Define the workflow (e.g., Workout Planner -> Nutrition Advisor -> Progress Tracker)
graph.add_edge(workout_planner, nutrition_advisor)
graph.add_edge(nutrition_advisor, progress_tracker)