import openai

import time

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

# lee un archivo y devuelve un array con las diapositivas
def read_article(file_name):
    file = open("/home/kali/github/Whisper/textos/" + file_name, "r")
    filedata = file.read()
    # print(filedata,"\n")
    return filedata.split("1.3"),numeroTokens(filedata)

# devuelve el numero de palabras de un texto
def numeroTokens(texto):
    palabras = texto.split()
    return len(palabras)
    
def getResusmenResumido(file_name, tamañoResumenFinal, palabrasParrafo, tokensMaxModelo):
    diapositivas, tokensTotales = read_article(file_name)
    diapositivas = filtrarFrases(diapositivas)
    print("Numero de tokens totales:", tokensTotales)
    print("Numero de diapositivas:", len(diapositivas))

    pasadasAcotadas = False

    if tamañoResumenFinal == 'mitad':
        tamañoResumenFinal = int(tokensTotales/2)
    elif tamañoResumenFinal == 'masmitad':
        tamañoResumenFinal = int(tokensTotales*(2/3))
    elif tamañoResumenFinal == 'extenso':
        tamañoResumenFinal = tokensTotales
    elif tamañoResumenFinal == int(tamañoResumenFinal):
        print(Fore.GREEN, "Número de pasadas:", tamañoResumenFinal, Style.RESET_ALL)
        pasadasAcotadas = True
    else:
        print(Fore.RED, "Error en el tamaño del resumen final", Style.RESET_ALL)
        return

    parrafos = getParrafos(diapositivas, palabrasParrafo, True)

    vecesResumidas = 0

    # stop por pasadas o por tamaño del resumen
    if pasadasAcotadas:
        stop = 2*tamañoResumenFinal
    else:
        stop = tamañoResumenFinal + 1

    while stop > tamañoResumenFinal:
        tamañoResumenes = 0
        vecesResumidas += 1
        resumenes = []
        for parrafo in parrafos:
            # prompt = "Sintetizame en " + str(int(len(parrafo.split())*(2/3))) + " o menos esto: " + parrafo
            prompt = "Sintatizame las siguientes diapositivas: " + parrafo
            # print("Prompt:", prompt)
            tokensPrompt = int((len(prompt.split())*2000)/1500)
            maxTokens = tokensMaxModelo - tokensPrompt
            tamañoResumen = 0
            i = 1
            while tamañoResumen == 0:
                response = chat(prompt, maxTokens)
                resumen = response["choices"][0]["text"]
                # print(response)
                tamañoResumen = len(resumen.split())
                if i >= 2 and tamañoResumen == 0:
                    print(Fore.RED, "Esperando para resumir el parrafo:", i, Style.RESET_ALL)
                    # esperamos 15 segundos para volver a resumir
                    time.sleep(15)
                    print(Fore.RED, "Volviendo a resumir el parrafo:", i, Style.RESET_ALL)
                i += 1          
            # print("Resumen:", resumen)
            resumenes.append(resumen)     
            tamañoResumenes += tamañoResumen
            print("Tamaño del resumen:", tamañoResumen)

        print(Fore.GREEN, "Tamaño de los resumenes:", tamañoResumenes, Style.RESET_ALL)
        parrafos = getParrafos(resumenes, palabrasParrafo, False)

        # stop por pasadas o por tamaño del resumen
        if pasadasAcotadas:
            stop -= 1
        else:
            stop = tamañoResumenes

    print("Numero de veces resumidas:", vecesResumidas)
    return parrafos

def filtrarFrases(sentences):
    # filtramos las frases que tengan menos de 6 palabras
    sentencesCopy = []
    for sentence in sentences:
        if len(sentence.split()) > 6:
            sentencesCopy.append(sentence)
    return sentencesCopy

# devuelve un array con los parrafos
def getParrafos(sentences, palabrasParrafo, sinpunto):
    parrafos = []
    parrafo = ""
    i = 0
    # variable boolena para inidcar que los parrafos son de la ia y no meter puntos al final
    if sinpunto:
        for sentence in sentences:
            if sentence == sentences[0]:
                parrafos.append(sentence + ". ")
            elif len(parrafos[i].split()) < palabrasParrafo:
                parrafos[i] += sentence + ". "
            else:
                parrafos.append(sentence + ". ")
                i += 1
    else:
        for sentence in sentences:
            if sentence == sentences[0]:
                parrafos.append(sentence)
            elif len(parrafos[i].split()) < palabrasParrafo:
                parrafos[i] += sentence
            else:
                parrafos.append(sentence)
                i += 1

    print("Numero de parrafos:", len(parrafos))
    tamañoFrases = []
    for sentence in sentences:
        tamañoFrases.append(len(sentence.split()))
    print("Tamaño de frases:", tamañoFrases)
    tamañoParrafos = []
    for parrafo in parrafos:
        tamañoParrafos.append(len(parrafo.split()))
    print("Tamaño de parrafos:", tamañoParrafos)
    return parrafos


# palabras que recibe chatgpt = entre 1900 y 2000 para recibir respuesta de 1000 mas o menos
# texto, tamañoResumen(mitad(1/2), masmitad(2/3), extenso(3/3)), palabrasParrafo, tokensMaxModelo
resumenResumido = getResusmenResumido("PRUEBA.txt", 1,  350, 3500)
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

