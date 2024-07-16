import requests
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI

class ProgressTracker:
    def __init__(self, api_key, tavily_api_key):
        self.llm = OpenAI(api_key=api_key)
        self.tavily_api_key = tavily_api_key

    def fetch_data_from_tavily(self, query):
        response = requests.get(f"https://api.tavily.com/query?query={query}&api_key={self.tavily_api_key}")
        return response.json()

    def track(self, user_preferences):
        progress_prompt = """
        You are a fitness tracker. Track the user's progress based on the following data:

        - Goal: {goal}
        - Completed Workouts: {completed_workouts}
        - Dietary Adherence: {dietary_adherence}
        - Weekly Summary: {weekly_summary}

        Provide feedback and motivation to help the user stay on track.
        """

        prompt = PromptTemplate(input_variables=["goal", "completed_workouts", "dietary_adherence", "weekly_summary"], template=progress_prompt)
        chain = LLMChain(prompt=prompt, llm=self.llm)
        progress = chain.run({
            "goal": user_preferences['goal'],
            "completed_workouts": user_preferences.get('completed_workouts', []),
            "dietary_adherence": user_preferences.get('dietary_adherence', 'None'),
            "weekly_summary": user_preferences.get('weekly_summary', 'None')
        })

        # Optionally fetch additional data from Tavily
        additional_data = self.fetch_data_from_tavily("motivation tips for fitness")
        progress["additional_data"] = additional_data

        return progress
