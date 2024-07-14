import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from workout_planner import WorkoutPlanner
from nutrition_advisor import NutritionAdvisor
from progress_tracker import ProgressTracker

def main():
    # Example user preferences
    user_preferences = {"goal": "build muscle", "experience": "beginner"}

    # Initialize agents
    workout_planner_agent = WorkoutPlanner()
    nutrition_advisor_agent = NutritionAdvisor()
    progress_tracker_agent = ProgressTracker()

    # Get plans and progress
    workout_plan = workout_planner_agent.create_plan(user_preferences)
    diet_plan = nutrition_advisor_agent.create_plan(user_preferences)
    progress = progress_tracker_agent.track(user_preferences)

    # Display results
    print("Workout Plan:", workout_plan)
    print("Diet Plan:", diet_plan)
    print("Progress:", progress)

    # Commenting out langgraph part
    """
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

    # Optionally, you can visualize the graph or run it to see the workflow in action
    graph.visualize()
    graph.run()
    """

if __name__ == "__main__":
    main()

