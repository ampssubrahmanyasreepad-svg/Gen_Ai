
import os
from dotenv import load_dotenv
from google import genai

print("Step 1: Loading environment variables...")

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

print("Step 2: Gemini API key loaded successfully.")

try:
    print("Step 3: Connecting to Gemini...")

    client = genai.Client(api_key=api_key)

    print("Step 4: Sending request to Gemini...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with: Gemini is working!"
    )

    print("\nStep 5: Response received!")
    print(response.text)

except Exception as error:
    print("\nAPI ERROR:")
    print(type(error).__name__)
    print(error)
