from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
app = Flask(__name__)

def summarize_meeting(text):

    sentences = text.split(".")

    # Meeting Summary
    summary = ". ".join(sentences[:3])

    # Key Points
    key_points = []
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 10:
            key_points.append(sentence)

    # Action Items
    action_items = []
    for sentence in sentences:
        if (
            "will" in sentence.lower()
            or "must" in sentence.lower()
            or "should" in sentence.lower()
        ):
            action_items.append(sentence.strip())

    result = f"""
MEETING SUMMARY
----------------
{summary}

KEY DISCUSSION POINTS
---------------------
"""

    for point in key_points[:5]:
        result += f"\n• {point}"

    result += "\n\nACTION ITEMS\n------------"

    if action_items:
        for item in action_items:
            result += f"\n• {item}"
    else:
        result += "\nNo action items found."

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    transcript = request.form["transcript"]

    result = summarize_meeting(transcript)

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)