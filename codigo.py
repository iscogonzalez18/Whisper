# código para la ejecución del programa whisper
# añadir la ruta al path
# export PATH=$PATH:/home/kali/.local/bin
# utilizar mejor simpleCode.py

import whisper
print(whisper.__file__)

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
naudio = "audio.mp3"
audio = whisper.load_audio("/home/kali/github/Whisper/audios/" + naudio)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}\n")

# decode the audio
options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

# print the recognized text
nfile = "marianTexto.txt"

file = open("/home/kali/github/Whisper/textos/" + nfile, "w")
print("file created\n")

print(result.text)

# escribimos todo el texto en un archivo con la funcion write
file.writelines(result.text)
print("audio printed in " + nfile + "\n")

file.close()
print("texto cerrado")
