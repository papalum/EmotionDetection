"""
Flask web server for emotion detection using Watson NLP.
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the main HTML page with the input form.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect_route():
    """
    Handles emotion detection requests.
    Returns a formatted string of emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(debug=True)
