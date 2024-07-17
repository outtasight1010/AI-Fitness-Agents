from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import openai  # Import openai for error handling

class ProgressTracker:
    def __init__(self, api_key, tavily_api_key):
        self.llm = OpenAI(api_key=api_key)
        self.tavily_api_key = tavily_api_key

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
        prompt_text = prompt.format(goal=user_preferences['goal'], completed_workouts=user_preferences['completed_workouts'], dietary_adherence=user_preferences['dietary_adherence'], weekly_summary=user_preferences['weekly_summary'])

        input_variables = {
            "goal": user_preferences['goal'],
            "completed_workouts": user_preferences.get('completed_workouts', []),
            "dietary_adherence": user_preferences.get('dietary_adherence', 'None'),
            "weekly_summary": user_preferences.get('weekly_summary', 'None')
        }
        print(f"Input Variables: {input_variables}")

        retries = 5
        for i in range(retries):
            try:
                response = self.llm.generate([prompt_text])
                progress = response.generations[0][0].text.strip()
                print(f"Generated Progress: {progress}")
                return progress
            except openai.error.RateLimitError as e:
                print(f"Rate limit exceeded. Retrying in {2 ** i} seconds...")
                time.sleep(2 ** i)
            except openai.error.OpenAIError as e:
                print(f"OpenAI Error: {e}")
                return {}
            except Exception as e:
                print(f"Error during LLM generate: {e}")
                return {}

        return {}




