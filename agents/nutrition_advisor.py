from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

class NutritionAdvisor:
    def __init__(self, api_key, tavily_api_key):
        self.llm = OpenAI(api_key=api_key)
        self.tavily_api_key = tavily_api_key

    def create_plan(self, user_preferences):
        nutrition_prompt = """
        You are a nutritionist. Create a dietary plan to complement the user's workout plan based on the following preferences:

        - Goal: {goal}
        - Dietary Restrictions: {dietary_restrictions}
        - Meal Preferences: {meal_preferences}

        Provide a daily meal plan with breakfast, lunch, dinner, and snacks.
        """

        prompt = PromptTemplate(input_variables=["goal", "dietary_restrictions", "meal_preferences"], template=nutrition_prompt)
        prompt_text = prompt.format(goal=user_preferences['goal'], dietary_restrictions=user_preferences['dietary_restrictions'], meal_preferences=user_preferences['meal_preferences'])

        input_variables = {
            "goal": user_preferences['goal'],
            "dietary_restrictions": user_preferences.get('dietary_restrictions', 'None'),
            "meal_preferences": user_preferences.get('meal_preferences', 'None')
        }
        print(f"Input Variables: {input_variables}")

        try:
            response = self.llm.generate(prompt_text)
            plan = response['choices'][0]['text'].strip()
            print(f"Generated Plan: {plan}")
        except Exception as e:
            print(f"Error during LLM generate: {e}")
            plan = {}

        return plan







