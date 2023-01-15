import openai

import nltk

# colores en el print
from colorama import Fore, Style
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print("Loading OpenAI GPT...")
openai.organization = "org-d6sOkmC5UFSQEz57mmi0kpzM"
openai.api_key = "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"

def chat(prompt, maxTokens):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=maxTokens,
        temperature=0.5,
    )
    return response

# lee un archivo y devuelve un array con las frases
def read_article(file_name):
    file = open("/home/kali/github/Whisper/textos/" + file_name, "r")
    filedata = file.read()
    # print(filedata,"\n")
    return filedata.split(". "),numeroTokens(filedata)

# devuelve el numero de palabras de un texto
def numeroTokens(texto):
    palabras = texto.split()
    return len(palabras)
    
def getResusmenResumido(file_name, tamañoResumenFinal, palabrasParrafo, tokensMaxModelo):
    sentences, tokensTotales = read_article(file_name)
    print("Numero de tokens totales:", tokensTotales)
    print("Numero de frases:", len(sentences))

    if tamañoResumenFinal == 'mitad':
        tamañoResumenFinal = int(tokensTotales/2)

    parrafos = getParrafos(sentences, palabrasParrafo)
    print("Numero de parrafos:", len(parrafos))
    tamañoFrases = []
    for sentence in sentences:
        tamañoFrases.append(len(sentence.split()))
    print("Tamaño de frases:", tamañoFrases)
    tamañoParrafos = []
    for parrafo in parrafos:
        tamañoParrafos.append(len(parrafo.split()))
    print("Tamaño de parrafos:", tamañoParrafos)
    
    vecesResumidas = 0
    tamañoResumenes = tamañoResumenFinal + 1
    while tamañoResumenes > tamañoResumenFinal:
        tamañoResumenes = 0
        vecesResumidas += 1
        resumenes = []
        for parrafo in parrafos:
            prompt = "Sintetizame esto: " + parrafo
            # print("Prompt:", prompt)
            tokensPrompt = int((len(prompt.split())*2000)/1500)
            maxTokens = tokensMaxModelo - tokensPrompt
            response = chat(prompt, maxTokens)
            resumen = response["choices"][0]["text"]
            print(response)
            # print("Resumen:", resumen)
            resumenes.append(resumen)
            tamañoResumen = len(resumen.split())
            tamañoResumenes += tamañoResumen
            print("Tamaño del resumen:", tamañoResumen)
        print(Fore.GREEN, "Tamaño de los resumenes:", tamañoResumenes, Style.RESET_ALL)
        parrafos = getParrafos(resumenes, palabrasParrafo)
    print("Numero de veces resumidas:", vecesResumidas)
    return parrafos

# devuelve un array con los parrafos
def getParrafos(sentences, palabrasParrafo):
    parrafos = []
    parrafo = ""
    i = 0
    for sentence in sentences:
        if sentence == sentences[0]:
            parrafos.append(sentence + ". ")
        elif len(parrafos[i].split()) < palabrasParrafo:
            parrafos[i] += sentence + ". "
        else:
            parrafos.append(sentence + ". ")
            i += 1
    return parrafos


# palabras que recibe chatgpt = entre 1900 y 2000 para recibir respuesta de 1000 mas o menos
# texto, tamañoResumen, palabrasParrafo, tokensMaxModelo
resumenResumido = getResusmenResumido("marianTexto.txt", 'mitad',  700, 3250)
for resumen in resumenResumido:
    print(resumen)

# while True:
#     prompt = input(Fore.CYAN + "\nEscribe tu pregunta, gracias para salir:\n" + Style.RESET_ALL)
#     if prompt == "gracias":
#         break

#     response = chat(prompt)

#     palabras = prompt.split()
#     print(Fore.BLUE + "Numero de palabras del input:", len(palabras), Style.RESET_ALL)

#     # print(response,"\n")
#     print(Fore.GREEN + Style.BRIGHT + response["choices"][0]["text"] + Style.RESET_ALL)

