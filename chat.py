import openai

# colores en el print
from colorama import Fore, Style
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print("Loading OpenAI GPT...")
openai.organization = "org-d6sOkmC5UFSQEz57mmi0kpzM"
openai.api_key = "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"

def chat(prompt):
    # https://beta.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2000
    )
    return response

# para leer un archivo
# archivo = open("archivo.txt", "r")
# prompt = archivo.read()

while True:
    prompt = input(Fore.CYAN + "\nEscribe tu pregunta, gracias para salir:\n" + Style.RESET_ALL)
    if prompt == "gracias":
        break

    response = chat(prompt)

    palabras = prompt.split()
    print(Fore.BLUE + "Numero de palabras del input:", len(palabras), Style.RESET_ALL)

    # print(response,"\n")
    print(Fore.GREEN + Style.BRIGHT + response["choices"][0]["text"] + Style.RESET_ALL)


