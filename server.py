"""Emotion detection module that uses the Watson NLP Emotion Predict service."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze the emotions in the given text using the Watson NLP API.

    Args:
        text_to_analyse (str): The text whose emotions should be detected.

    Returns:
        dict: The scores for anger, disgust, fear, joy and sadness, plus the
        dominant emotion (the emotion with the highest score). If the API
        returns status code 400 (for example, for a blank entry), every
        value in the dictionary is None.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
