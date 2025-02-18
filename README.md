# Business Card Scanner API

A Flask-based REST API that extracts and structures information from business card images using OCR and AI.

## Features

- Supports multiple OCR engines:
  - Google Cloud Vision API
  - Tesseract OCR
- Text structuring using OpenAI GPT
- JSON output format
- File upload validation
- Secure file handling
- Configurable via environment variables

## Tech Stack

- Python 3.x
- Flask 2.0.1
- Google Cloud Vision API
- OpenAI GPT API
- Tesseract OCR
- Additional dependencies in `requirements.txt`

## Prerequisites

1. Python 3.10 or higher
2. Tesseract OCR installed on your system
3. Google Cloud account
4. OpenAI account
5. Git (optional)

## Installation

1. Clone the repository (or download the source code):

   ```bash
   git clone https://github.com/The-Lone-Druid/cardscannerpoc.git
   cd cardscannerpoc
   ```

2. Create and activate a virtual environment:

   ```bash
   # Windows
   python -m venv venv
   source venv/Scripts/activate  # Git Bash
   # or
   .\venv\Scripts\activate.ps1   # PowerShell
   # or
   venv\Scripts\activate.bat     # Command Prompt

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

### 1. Google Cloud Vision API

1. Create a Google Cloud account: [https://cloud.google.com/](https://cloud.google.com/)
2. Create a new project in Google Cloud Console
3. Enable the Cloud Vision API:
   - Go to "APIs & Services" > "Library"
   - Search for "Cloud Vision API"
   - Click "Enable"
   - Make sure to add a billing account to the project or else the API will not work, follow the instructions [here](https://cloud.google.com/vision/docs/billing)
4. Create credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Fill in service account details
   - Select role: "Project" > "Owner"
   - Click "Create and Continue"
5. Download JSON credentials:
   - Click on your service account
   - Go to "Keys" tab
   - Click "Add Key" > "Create New Key"
   - Choose JSON format
   - Save the file in your project's `credentials` folder

### 2. OpenAI API

1. Create an OpenAI account: [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. Get your API key:
   - Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Click "Create new secret key"
   - Copy the generated key
   - This also requires a billing account, follow the instructions [here](https://platform.openai.com/docs/billing)

### 3. Tesseract OCR

1. Windows:

   - Download installer from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install and note the installation path
   - Update `tesseract_cmd` path in `utils/tesseract_helper.py`

2. macOS:

   ```bash
   brew install tesseract
   ```

3. Linux:

   ```bash
   sudo apt-get install tesseract-ocr
   ```

## Configuration

1. Create a `.env` file in the project root:

   ```env
   FLASK_SECRET_KEY=your-secret-key-here
   GOOGLE_APPLICATION_CREDENTIALS=./credentials/your-credentials-file.json
   OPENAI_API_KEY=your-openai-api-key
   ```

2. Create required directories:

   ```bash
   mkdir -p credentials
   mkdir -p scans/generated
   ```

3. Move your Google Cloud credentials JSON file to the `credentials` folder

## Test your setup

```bash
python test_setup.py
```

Once you have verified that the API keys are working, you can start the application.

## Running the Application

1. Ensure your virtual environment is activated

2. Start the Flask server:

   ```bash
   python app.py
   ```

3. Access the application at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage

1. Open the web interface in your browser
2. Select the OCR engine (Google Vision or Tesseract)
3. Upload a business card image
4. Click "Scan Card"
5. View the extracted information in both raw and structured JSON format

## Project Structure

```text
cardscannerpoc/
├── __pycache__/
├── credentials/
├── scans/
│   └── generated/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── utils/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── vision_helper.py
│   ├── tesseract_helper.py
│   └── gpt_helper.py
├── .env
├── .gitignore
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── test_setup.py
└── TODOS.md
```

## Testing

Test your API connections:

```bash
python test_setup.py
```

## Error Handling

The application includes error handling for:

- Invalid file types
- Failed text extraction
- API connection issues
- Processing errors

## Security Notes

1. Never commit sensitive files:

   - .env
   - API credentials
   - Uploaded images
   - Generated JSON files

2. The .gitignore file is configured to exclude:
   - Sensitive files
   - Virtual environment
   - Python cache files
   - Uploaded and generated files

## TODOs

1. Integration with Deepseek R1 Model
2. Cost estimation for various APIs
3. Project documentation enhancement
4. Microservice implementation with Node.js integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Commitizen

This project uses Commitizen for commit messages. To commit, you'll have to install commitizen and setup husky:

1. Install dependencies:

   ```bash
   npm install
   ```

2. Initialize husky:

   ```bash
   npx husky install
   ```

3. Commit using Commitizen:

   ```bash
    git commit
    # or
    npm run commit
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
