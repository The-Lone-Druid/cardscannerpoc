let currentRotation = 0;

// Add image preview functionality
document.getElementById('cardImage').addEventListener('change', function(e) {
    const imagePreview = document.getElementById('imagePreview');
    const rotationControls = document.getElementById('rotationControls');
    imagePreview.innerHTML = ''; // Clear previous preview
    currentRotation = 0; // Reset rotation
    
    if (e.target.files && e.target.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            imagePreview.appendChild(img);
            imagePreview.style.display = 'block';
            rotationControls.style.display = 'block';
        }
        
        reader.readAsDataURL(e.target.files[0]);
    } else {
        imagePreview.style.display = 'none';
        rotationControls.style.display = 'none';
    }
});

// Add rotation event listeners
document.querySelectorAll('.rotate-btn').forEach(button => {
    button.addEventListener('click', function() {
        const degrees = parseInt(this.dataset.degrees);
        const img = document.querySelector('#imagePreview img');
        if (img) {
            currentRotation = (currentRotation + degrees) % 360;
            img.style.transform = `rotate(${currentRotation}deg)`;
        }
    });
});

document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const fileInput = document.getElementById('cardImage');
    const ocrEngine = document.getElementById('ocrEngine');
    const resultDiv = document.getElementById('result');
    const structuredDataDiv = document.getElementById('structuredData');
    const rawTextDiv = document.getElementById('rawText');
    
    if (!fileInput.files[0]) {
        alert('Please select a file');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('ocr_engine', ocrEngine.value);
    formData.append('rotation', currentRotation); // Add rotation angle
    
    try {
        resultDiv.style.display = 'block';
        structuredDataDiv.innerHTML = 'Processing...';
        rawTextDiv.innerHTML = '';
        
        const response = await fetch('/scan', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            structuredDataDiv.innerHTML = `
                <h3>Structured Information:</h3>
                <pre>${JSON.stringify(data.result, null, 2)}</pre>
            `;
            rawTextDiv.innerHTML = `
                <h3>Raw Extracted Text:</h3>
                <pre>${data.raw_text}</pre>
            `;
        } else {
            structuredDataDiv.innerHTML = `<div class="error">Error: ${data.error}</div>`;
            rawTextDiv.innerHTML = '';
        }
    } catch (error) {
        structuredDataDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
        rawTextDiv.innerHTML = '';
    }
}); 