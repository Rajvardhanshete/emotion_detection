import json
import requests

def emotion_detector(text_to_analyse):
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        myobj = { "raw_document": { "text": text_to_analyse } }
        response = requests.post(url=url, json=myobj, headers= header)
        formatted_response = json.loads(response.text)
        # Extract emotion predictions
        emotion_predictions = formatted_response.get('emotionPredictions', [])

        if not emotion_predictions:
            return {"error": "No emotion predictions found in the response"}

        # Get the emotion values from the first prediction (assuming there's at least one)
        emotions = emotion_predictions[0]['emotion']
        
        # Store each emotion score in variables
        emotion_scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }

        # Find the dominant emotion based on the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the emotion scores and the dominant emotion
        return {
            "anger": emotion_scores['anger'],
            "disgust": emotion_scores['disgust'],
            "fear": emotion_scores['fear'],
            "joy": emotion_scores['joy'],
            "sadness": emotion_scores['sadness'],
            "dominant_emotion": dominant_emotion
        }