import base64
import wave

sound_data = open('19-mail.txt', 'r').read()

first_try = open("indian_1.wav", "wb")
decodestring = base64.decodestring(sound_data)
first_try.write(decodestring)

# sorry -> what you apologizing for

first_try_2 = wave.open("indian_1.wav", 'r')
fh = wave.open("indian_2.wav", "wb")

fh.setnchannels(first_try_2.getnchannels())
fh.setsampwidth(first_try_2.getsampwidth())
fh.setframerate(first_try_2.getframerate() * 2)

fh.writeframes(decodestring)
