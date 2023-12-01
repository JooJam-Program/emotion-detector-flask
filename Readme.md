# Emotion Detector Flask Microservice

## Overview
This Flask microservice integrates NLP models from Hugging Face, demonstrating an emotion detection application using "SamLowe/roberta-base-go_emotions" model. It's an example adaptable for various NLP use cases.

## Prerequisites
- Python 3.6+
- Virtual Environment

## Setup Instructions
1. **Check Python Version**:
   `python3 --version`
2. **Clone Repository**:
   `git clone https://github.com/your-username/emotion-detector-flask.git`
3. **Virtual Environment**:
   - Create: `python3 -m venv venv` you can change the name `venv` to your liking
   - Activate: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. **Install Dependencies**:
   - `pip install -r requirements.txt`
   - Install PyTorch as per [PyTorch website](https://pytorch.org/get-started/locally/).

## Running the Application
1. **Start Flask App**:
   `python run.py`
2. **API Endpoint**:
   Accessible at `http://127.0.0.1:5000/`.
   You can communicate with `/emotion` endpoint for now from `route.py` and eventually add some more.

## Customizing the Model
To use a different Hugging Face model:
1. Update `model_name` in `app/model.py`.
2. Adjust `task` parameter as required.

## Best Practices
- Use virtual environments for dependency management.
- Regularly update `requirements.txt` to keep track of dependencies with `pip freeze > requirements.txt`.
- Follow PEP 8 guidelines for Python code.
- Structure code modularly for maintainability and scalability.
- Create a `.env.local` for you environment variables.

## Contributing
Contributions are welcome. Please fork the repository and submit pull requests.
