
import whisper

naudio = "GP-Tema-1p1.mp3"
language_whisper = "Spanish"
model = whisper.load_model("small")

# Set options
options = dict(language=language_whisper)
transcribe_options = dict(task="transcribe", **options)

result = model.transcribe("/home/kali/github/Whisper/audios/" + naudio, **transcribe_options)["text"]

# print the recognized text
nfile = "GP-Tema-1p1.txt"

file = open("/home/kali/github/Whisper/textos/" + nfile, "w")
print("file created\n")

# escribimos todo el texto en un archivo con la funcion write
file.writelines(result)
print("audio printed in " + nfile + "\n")

file.close()
print("texto cerrado")