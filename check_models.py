import os
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key not found.")
    exit(1)

# Initialize Client
client = genai.Client(api_key=api_key)

print("Fetching available models...\n")

try:
    for model in client.models.list():
        print(f"- {model.name}")
except Exception as e:
    print(f"Error fetching models: {e}")