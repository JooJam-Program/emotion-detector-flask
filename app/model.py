from transformers import pipeline

# you can change the model name here and the task for other models
model_name = "SamLowe/roberta-base-go_emotions"
classifier = pipeline(task="text-classification", model=model_name, top_k=None)

def get_emotion(text):
    # Get emotion prediction
    model_outputs = classifier(text)
    return model_outputs
