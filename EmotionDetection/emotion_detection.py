import json
import requests

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=myobj, headers= header)
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotion']['document']

# Store each emotion in a separate variable
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return { " anger":anger, "disgust": disgust, "fear": fear, 
    "joy": joy, "sadness": sadness, 
    "dominant_emotion": dominant_emotion }