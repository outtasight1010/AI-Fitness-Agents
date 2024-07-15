from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class ProgressTracker:
    def __init__(self):
        self.llm = OpenAI()

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
        return progress

