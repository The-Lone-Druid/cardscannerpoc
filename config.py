import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'your-secret-key')
    UPLOAD_FOLDER = 'scans/generated'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    
    # API Keys
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 