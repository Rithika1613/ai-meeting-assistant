def create_prompt(transcript):
    return f"""
You are an AI Meeting Assistant.

Analyze the following meeting transcript.

Provide:

1. Meeting Summary
2. Key Discussion Points
3. Action Items
4. Decisions Made
5. Next Steps

Meeting Transcript:

{transcript}
"""