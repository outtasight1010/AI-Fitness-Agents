import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
tavily_api_key = os.getenv('TAVILY_API_KEY')

print(f"OpenAI API Key: {openai_api_key}")
print(f"Tavily API Key: {tavily_api_key}")
