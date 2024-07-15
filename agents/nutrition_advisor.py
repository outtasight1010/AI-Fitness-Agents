from langchain import LLM, PromptTemplate, generate

class NutritionAdvisor:
    def __init__(self):
        self.llm = LLM()

    def create_plan(self, user_preferences):
        nutrition_prompt = """
        You are a nutritionist. Create a dietary plan to complement the user's workout plan based on the following preferences:

        - Goal: {goal}
        - Dietary Restrictions: {dietary_restrictions}
        - Meal Preferences: {meal_preferences}

        Provide a daily meal plan with breakfast, lunch, dinner, and snacks.
        """

        prompt = PromptTemplate(nutrition_prompt)
        input_text = prompt.format(goal=user_preferences['goal'], dietary_restrictions=user_preferences.get('dietary_restrictions', 'None'), meal_preferences=user_preferences.get('meal_preferences', 'None'))
        plan = generate(self.llm, input_text)
        return plan

