import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from workout_planner import WorkoutPlanner
from nutrition_advisor import NutritionAdvisor
from progress_tracker import ProgressTracker

def main():
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

if __name__ == "__main__":
    main()
