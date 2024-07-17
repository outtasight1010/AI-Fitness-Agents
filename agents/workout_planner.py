import requests
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI

class WorkoutPlanner:
    def __init__(self, api_key, tavily_api_key):
        self.llm = OpenAI(api_key=api_key)
        self.tavily_api_key = tavily_api_key

    def fetch_data_from_tavily(self, query):
        response = requests.get(f"https://api.tavily.com/query?query={query}&api_key={self.tavily_api_key}")
        return response.json()

    def create_plan(self, user_preferences):
        workout_prompt = """
        You are a fitness coach. Create a personalized workout plan for the user based on the following preferences:

        - Goal: {goal}
        - Experience: {experience}

        Provide a weekly workout plan with exercises, sets, and repetitions.
        """

        prompt = PromptTemplate(input_variables=["goal", "experience"], template=workout_prompt)
        chain = LLMChain(prompt=prompt, llm=self.llm)

        # Debug prints to check the prompt and the user preferences
        print(f"User Preferences: {user_preferences}")
        input_variables = {"goal": user_preferences['goal'], "experience": user_preferences['experience']}
        print(f"Input Variables: {input_variables}")

        try:
            plan = chain.run(input_variables)
            print(f"Generated Plan: {plan}")
        except Exception as e:
            print(f"Error during chain.run: {e}")
            plan = {}

        # Fetch additional data from Tavily
        additional_data = self.fetch_data_from_tavily("fitness tips for beginners")
        plan["additional_data"] = additional_data

        return plan



