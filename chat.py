import openai

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

prompt = "sintetizame el siguiente texto: Definición oUn asistente virtual es un agente de software que ayuda a usuarios de sistemas computacionales, automatizando y realizando tareas con la mínima interacción hombre-máquina Dispositivos con asistentes virtuales oAltavoces inteligentes (Amazon Echo, Google Home) oAplicaciones de mensajería instantánea (Whatsapp) oComo parte del sistema operativo (Siri, Cortana) oEn un modelo de teléfono concreto (Bixby) oAplicaciones móviles específicas (Cortana, Google Assistant) oRelojes inteligentes oElectrodomésticos"

response = chat(prompt)

# para leer un archivo
# archivo = open("archivo.txt", "r")
# prompt = archivo.read()

palabras = prompt.split()
print("Numero de palabras del input:", len(palabras))

print(response,"\n")
print(response["choices"][0]["text"])

