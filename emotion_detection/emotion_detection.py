

import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    # Handle empty or invalid input (HTTP 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()
    emotion_scores = response_json['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': emotion_scores.get('anger'),
        'disgust': emotion_scores.get('disgust'),
        'fear': emotion_scores.get('fear'),
        'joy': emotion_scores.get('joy'),
        'sadness': emotion_scores.get('sadness'),
        'dominant_emotion': dominant_emotion
    }
