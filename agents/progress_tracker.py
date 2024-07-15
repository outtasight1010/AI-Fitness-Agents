from langchain import LLM, PromptTemplate, generate

class ProgressTracker:
    def __init__(self):
        self.llm = LLM()

    def track(self, user_preferences):
        progress_prompt = """
        You are a fitness tracker. Track the user's progress based on the following data:

        - Goal: {goal}
        - Completed Workouts: {completed_workouts}
        - Dietary Adherence: {dietary_adherence}
        - Weekly Summary: {weekly_summary}

        Provide feedback and motivation to help the user stay on track.
        """

        prompt = PromptTemplate(progress_prompt)
        input_text = prompt.format(goal=user_preferences['goal'], completed_workouts=user_preferences.get('completed_workouts', []), dietary_adherence=user_preferences.get('dietary_adherence', 'None'), weekly_summary=user_preferences.get('weekly_summary', 'None'))
        progress = generate(self.llm, input_text)
        return progress
