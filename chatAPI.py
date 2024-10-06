from openai import OpenAI
from pathlib import Path
client = OpenAI(api_key="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")
def audioToText(file):
    audio_file= open(file, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    return transcript


def textToAudio(trans):
    speech_file_path = Path(__file__).parent / "ttsThing.mp3"
    response= client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=trans
        )
    response.stream_to_file(speech_file_path)

def prompt(prompt):

    completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
    {"role": "system", "content": "Your are a game-master, your job is to check to see if a given word is similar to the theme if so then output true, else false. There must be no spelling-errors within the answer and they have to do with the theme"},
    {"role": "user", "content": prompt}
  ]
    )

    return completion.choices[0].message.content

    
