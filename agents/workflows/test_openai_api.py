import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Print the API key to verify
print(f"OpenAI API Key: {openai_api_key}")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Test prompt
prompt = "What is the capital of France?"

# Generate response
try:
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50
    )
    print(f"Response: {response.choices[0].text.strip()}")
except Exception as e:
    print(f"Error: {e}")

