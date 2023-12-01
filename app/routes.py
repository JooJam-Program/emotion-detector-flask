from app import app
from flask import request, jsonify
from app.model import get_emotion

@app.route('/emotion', methods=['POST'])
def emotion():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = get_emotion(text)
    return jsonify(result)
