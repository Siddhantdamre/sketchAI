from flask import Flask, render_template, request, send_file
import speech_to_text, text_processing, generate_sketch

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Capture audio and convert to text
    description = speech_to_text.capture_audio()
    
    # Extract features from description
    features = text_processing.extract_features(description)
    
    # Generate sketch based on features
    image_path = generate_sketch.create_sketch(features)
    
    # Display the generated image
    return render_template('index.html', image_path=image_path, description=description)

if __name__ == '__main__':
    app.run(debug=True)
