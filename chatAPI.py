from openai import OpenAI
from pathlib import Path
#Removed api key for public but api key goes in here
client = OpenAI(api_key="api key here")

#function for taking audio and outputting text
def audioToText(file):
    #open audio file
    audio_file= open(file, "rb")
    #Create transcript using the openAI whisper-1 model and respond in text format
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    
    #Return text format
    return transcript

#Unused for now but for changing text to audio using openAI tts-1 with the alloy voice
def textToAudio(trans):
    #using 
    speech_file_path = Path(__file__).parent / "ttsThing.mp3"
    response= client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=trans
        )
    response.stream_to_file(speech_file_path)


#Used to compare the word said to the theme
def prompt(prompt):
    #completion[0] is the return text (true or false) 
    completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
    {"role": "system", "content": "Your are a game-master, your job is to check to see if a given word is similar to the theme if so then output true, else false. There must be no spelling-errors within the answer and they have to do with the theme"},
    {"role": "user", "content": prompt}
  ]
    )

    return completion.choices[0].message.content

    
