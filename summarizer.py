import re

def summarize(text):
    sentences = text.split(".")

    summary = ".".join(sentences[:3])

    actions = []

    for sentence in sentences:
        if "will" in sentence.lower():
            actions.append(sentence.strip())

    return summary, actions