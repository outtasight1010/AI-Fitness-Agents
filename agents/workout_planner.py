from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import openai  # Import openai for error handling

class WorkoutPlanner:
    def __init__(self, api_key, tavily_api_key):
        self.llm = OpenAI(api_key=api_key)
        self.tavily_api_key = tavily_api_key

    def create_plan(self, user_preferences):
        workout_prompt = """
        You are a fitness coach. Create a personalized workout plan for the user based on the following preferences:

        - Goal: {goal}
        - Experience: {experience}

        Provide a weekly workout plan with exercises, sets, and repetitions.
        """

        prompt = PromptTemplate(input_variables=["goal", "experience"], template=workout_prompt)
        prompt_text = prompt.format(goal=user_preferences['goal'], experience=user_preferences['experience'])

        input_variables = {"goal": user_preferences['goal'], "experience": user_preferences['experience']}
        print(f"Input Variables: {input_variables}")

        retries = 5
        for i in range(retries):
            try:
                response = self.llm.generate([prompt_text])
                plan = response.generations[0][0].text.strip()
                print(f"Generated Plan: {plan}")
                return plan
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










