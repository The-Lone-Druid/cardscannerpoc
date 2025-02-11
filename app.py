import os
import json
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from config import Config
from utils.vision_helper import VisionHelper
from utils.tesseract_helper import TesseractHelper
from utils.gpt_helper import GPTHelper

app = Flask(__name__)
app.config.from_object(Config)

vision_helper = VisionHelper()
tesseract_helper = TesseractHelper()
gpt_helper = GPTHelper()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_card():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    ocr_engine = request.form.get('ocr_engine', 'google_vision')  # Default to Google Vision
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Save the uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text using selected OCR engine
            if ocr_engine == 'tesseract':
                extracted_text = tesseract_helper.extract_text(filepath)
            else:  # google_vision
                extracted_text = vision_helper.extract_text(filepath)

            if not extracted_text:
                return jsonify({'error': 'No text could be extracted from the image'}), 400
            
            # Structure the text using GPT
            structured_data = gpt_helper.structure_text(extracted_text)
            
            # Save the JSON result
            json_filename = f"{os.path.splitext(filename)[0]}_result.json"
            json_filepath = os.path.join(app.config['UPLOAD_FOLDER'], json_filename)
            
            with open(json_filepath, 'w') as f:
                f.write(structured_data)
            
            return jsonify({
                'result': json.loads(structured_data),
                'raw_text': extracted_text  # Adding raw text for comparison
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True) 