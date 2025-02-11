import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

class GPTHelper:
    @staticmethod
    def structure_text(text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a business card information extractor. 
                        Extract the following fields from the text and return them in JSON format:
                        - name
                        - job_title
                        - company
                        - email
                        - phone_numbers (as array)
                        - address
                        - website
                        - social_media_links (as array)
                        
                        If a field is not found, set it to null."""
                    },
                    {
                        "role": "user",
                        "content": f"Extract information from this business card text:\n{text}"
                    }
                ],
                temperature=0.3
            )
            
            return response.choices[0].message['content']
        
        except Exception as e:
            print(f"Error in GPT processing: {str(e)}")
            return "{}" 