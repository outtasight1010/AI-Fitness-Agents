from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class NutritionAdvisor:
    def __init__(self):
        self.llm = OpenAI()

    def create_plan(self, user_preferences):
        nutrition_prompt = """
        You are a nutritionist. Create a dietary plan to complement the user's workout plan based on the following preferences:

        - Goal: {goal}
        - Dietary Restrictions: {dietary_restrictions}
        - Meal Preferences: {meal_preferences}

        Provide a daily meal plan with breakfast, lunch, dinner, and snacks.
        """

        prompt = PromptTemplate(input_variables=["goal", "dietary_restrictions", "meal_preferences"], template=nutrition_prompt)
        chain = LLMChain(prompt=prompt, llm=self.llm)
        plan = chain.run({
            "goal": user_preferences['goal'],
            "dietary_restrictions": user_preferences.get('dietary_restrictions', 'None'),
            "meal_preferences": user_preferences.get('meal_preferences', 'None')
        })
        return plan


