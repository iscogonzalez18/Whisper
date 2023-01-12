import openai
import os

openai.organization = "org-"
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response

prompt = "Human: Hello, who are you?"

print(chat(prompt))
