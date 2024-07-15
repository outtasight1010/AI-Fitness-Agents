from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class WorkoutPlanner:
    def __init__(self):
        self.llm = OpenAI()

    def create_plan(self, user_preferences):
        workout_prompt = """
        You are a fitness coach. Create a personalized workout plan for the user based on the following preferences:

        - Goal: {goal}
        - Experience: {experience}

        Provide a weekly workout plan with exercises, sets, and repetitions.
        """

        prompt = PromptTemplate(input_variables=["goal", "experience"], template=workout_prompt)
        chain = LLMChain(prompt=prompt, llm=self.llm)
        plan = chain.run({"goal": user_preferences['goal'], "experience": user_preferences['experience']})
        return plan


