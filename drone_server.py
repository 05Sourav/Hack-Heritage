from flask import Flask,request,jsonify 
import os 

app=Flask(__name__)

UPLOAD_FOLDER='/vir/lib/Mysql/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the image to the specified directory
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    return jsonify({'message': 'Image received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
