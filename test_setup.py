import os
from google.cloud import vision
import openai
from dotenv import load_dotenv

load_dotenv()

def test_vision_api():
    try:
        client = vision.ImageAnnotatorClient()
        print("✅ Google Cloud Vision credentials loaded successfully")
    except Exception as e:
        print("❌ Google Cloud Vision Error:", str(e))

def test_openai_api():
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello!"}],
            max_tokens=5
        )
        print("✅ OpenAI API connection successful")
    except Exception as e:
        print("❌ OpenAI Error:", str(e))

if __name__ == "__main__":
    print("Testing API Connections...")
    test_vision_api()
    test_openai_api() 