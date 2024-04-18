from gtts import gTTS

words = ['help', 'seat', 'rock', 'tired', 'connect', "what's up", 'cannot', 'where', 'please', 'wifi', 'i', 'thank you']
# words = ['help', 'seat', 'rock', 'tired', 'connect', "what's up", 'cannot', 'where', 'please', 'wifi', 'i', 'thank you']

for word in words:
    tts = gTTS(text=word, lang='en')
    filename = f"{word}.mp3"
    tts.save(filename)
    print(f"Generated TTS for '{word}' as '{filename}'")