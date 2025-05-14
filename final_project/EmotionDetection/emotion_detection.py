# Import the requests library to handle HTTP requests, import json for parsing
import requests
import json

def emotion_detector(text_to_analyze): #Function to detect emotion
    # URL of motion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary of text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Set headers the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST response to the API with text and headers
    response = requests.post(url, json = myobj, headers=header) 
    res = response.json()

    # Extracting emotion label from the response
    emotions = res['emotionPredictions'][0]['emotion']
    emotion_scores = {
    
    'anger': emotions ["anger"],
    'disgust': emotions ["disgust"],
    'fear': emotions ["fear"],
    'joy': emotions ["joy"],
    'sadness': emotions ["sadness"]}

    # Extract the max emotion rating from the response
    dominant_emotion = max(emotion_scores, key = emotion_scores.get)

    # Return a response with text from the API
    return {'anger':  emotion_scores['anger'],'disgust':  emotion_scores ['disgust'],'fear':  emotion_scores['fear'],'joy':  emotion_scores['joy'],
    'sadness':  emotion_scores['sadness'],
    'dominant_emotion': dominant_emotion}
