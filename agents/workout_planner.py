from langchain import LLM, PromptTemplate, generate

class WorkoutPlanner:
    def __init__(self):
        self.llm = LLM()
    #Prompt creation
    def create_plan(self, user_preferences):
        workout_prompt = """
        You are a fitness coach. Create a personalized workout plan for the user based on the following preferences:

        - Goal: {goal}
        - Experience: {experience}

        Provide a weekly workout plan with exercises, sets, and repetitions.
        """
        # An example of a generated workout, according to goal, experience level
        prompt = PromptTemplate(workout_prompt)
        input_text = prompt.format(goal=user_preferences['goal'], experience=user_preferences['experience'])
        plan = generate(self.llm, input_text)
        return plan

