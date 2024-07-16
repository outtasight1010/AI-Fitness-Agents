import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from workout_planner import WorkoutPlanner
from nutrition_advisor import NutritionAdvisor
from progress_tracker import ProgressTracker
from langgraph import Graph, Node

def main():
    # Get the API keys from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    tavily_api_key = os.getenv('TAVILY_API_KEY')

    # Check if the API keys are set
    if not openai_api_key:
        raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    if not tavily_api_key:
        raise ValueError("No Tavily API key found. Please set the TAVILY_API_KEY environment variable.")

    # Example user preferences
    user_preferences = {
        "goal": "build muscle",
        "experience": "beginner",
        "dietary_restrictions": "None",
        "meal_preferences": "None",
        "completed_workouts": [],
        "dietary_adherence": "None",
        "weekly_summary": "None"
    }

    # Initialize agents with API keys
    workout_planner_agent = WorkoutPlanner(api_key=openai_api_key, tavily_api_key=tavily_api_key)
    nutrition_advisor_agent = NutritionAdvisor(api_key=openai_api_key, tavily_api_key=tavily_api_key)
    progress_tracker_agent = ProgressTracker(api_key=openai_api_key, tavily_api_key=tavily_api_key)

    # Get plans and progress
    workout_plan = workout_planner_agent.create_plan(user_preferences)
    diet_plan = nutrition_advisor_agent.create_plan(user_preferences)
    progress = progress_tracker_agent.track(user_preferences)

    # Display results
    print("Workout Plan:", workout_plan)
    print("Diet Plan:", diet_plan)
    print("Progress:", progress)

    # Define nodes for each agent
    workout_planner_node = Node(name="Workout Planner", function=workout_planner_agent.create_plan, args=[user_preferences])
    nutrition_advisor_node = Node(name="Nutrition Advisor", function=nutrition_advisor_agent.create_plan, args=[user_preferences])
    progress_tracker_node = Node(name="Progress Tracker", function=progress_tracker_agent.track, args=[user_preferences])

    # Create a graph and add nodes
    graph = Graph()
    graph.add_node(workout_planner_node)
    graph.add_node(nutrition_advisor_node)
    graph.add_node(progress_tracker_node)

    # Define the workflow (e.g., Workout Planner -> Nutrition Advisor -> Progress Tracker)
    graph.add_edge(workout_planner_node, nutrition_advisor_node)
    graph.add_edge(nutrition_advisor_node, progress_tracker_node)

    # Run the graph to see the workflow in action
    graph.run()

if __name__ == "__main__":
    main()
