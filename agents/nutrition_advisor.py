class NutritionAdvisor:
    def __init__(self):
        pass

    def create_plan(self, user_preferences):
        # Mock implementation of diet plan creation
        goal = user_preferences.get("goal", "general fitness")
        
        plan = {
            "goal": goal,
            "meals": [
                {"meal": "Breakfast", "food": "Oatmeal with fruits"},
                {"meal": "Lunch", "food": "Grilled chicken with vegetables"},
                {"meal": "Dinner", "food": "Salmon with quinoa"}
            ]
        }
        return plan
