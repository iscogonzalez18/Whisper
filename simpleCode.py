
import whisper

naudio = "audio.mp3"

model = whisper.load_model("base")
result = model.transcribe("/home/kali/github/Whisper/audios/" + naudio)
print(result["text"])

# print the recognized text
nfile = "marianTexto.txt"

file = open("/home/kali/github/Whisper/textos/" + nfile, "w")
print("file created\n")

# escribimos todo el texto en un archivo con la funcion write
file.writelines(result["text"])
print("audio printed in " + nfile + "\n")

file.close()
print("texto cerrado")