from google.cloud import vision
import io

class VisionHelper:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def extract_text(self, image_path):
        try:
            with io.open(image_path, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            response = self.client.text_detection(image=image)
            texts = response.text_annotations

            if texts:
                return texts[0].description
            
            return ""

        except Exception as e:
            print(f"Error in text extraction: {str(e)}")
            return "" 