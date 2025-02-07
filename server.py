from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    return response
    # # Extract the label and score from the response
    # label = response['dominant_emotion']
    # score = response['score']

    # # Check if the label is None, indicating an error or invalid input
    # if label is None:
    #     return "Invalid input! Try again."
    # else:
    #     # Return a formatted string with the sentiment label and score
    #     return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
