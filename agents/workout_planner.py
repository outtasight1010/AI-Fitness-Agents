class WorkoutPlanner:
    def __init__(self):
        pass

    def create_plan(self, user_preferences):
        # Mock implementation of workout plan creation
        goal = user_preferences.get("goal", "general fitness")
        experience = user_preferences.get("experience", "beginner")
        
        plan = {
            "goal": goal,
            "experience": experience,
            "workouts": [
                {"day": "Monday", "exercise": "Push-ups", "reps": 10},
                {"day": "Wednesday", "exercise": "Squats", "reps": 15},
                {"day": "Friday", "exercise": "Plank", "time": "1 min"}
            ]
        }
        return plan
