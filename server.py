# server.py

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect_route():
    text_to_analyze = request.args.get("textToAnalyze", "")
    
    if not text_to_analyze.strip():
        return "Error: No text provided for analysis."

    result = emotion_detector(text_to_analyze)

    # Format the response as per the example
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
