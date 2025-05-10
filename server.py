# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created: TODO
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('text_to_analyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    emotion = response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    #dominant_emotion = response['dominant_emotion']
    
    #Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
       response_text = "Invalid Input! Please try again."
    response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

    # TODO

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
    #TODO