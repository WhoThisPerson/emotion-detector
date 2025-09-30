"""
Flask server for the Emotion Detector web application.
This server exposes two routes:
- "/" to render the index page
- "/emotionDetector" to analyze text and return emotion scores
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint that analyzes the given text and returns
    the emotion scores along with the dominant emotion.
    """
    text = request.args.get("textToAnalyze")

    response = emotion_detector(text)

    anger_score = response.get("anger", 0)
    disgust_score = response.get("disgust", 0)
    fear_score = response.get("fear", 0)
    joy_score = response.get("joy", 0)
    sadness_score = response.get("sadness", 0)
    dominant_emotion = response.get("dominant_emotion", 0)

    if dominant_emotion is not None:

        responded_text = (
            f"For the given statement, the system response is "
            f"'anger': {anger_score}, "
            f"'disgust': {disgust_score}, "
            f"'fear': {fear_score}, "
            f"'joy': {joy_score} and "
            f"'sadness': {sadness_score}. "
            f"The dominant emotion is {dominant_emotion}."
        )
    else:
        responded_text = "Invalid text! Please try again!"
    return responded_text

@app.route("/")
def render_index_page():
    """
    Renders the index.html page, which contains
    the UI for submitting text to analyze.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
