import openai
import os

print("Loading OpenAI GPT...")
openai.organization = "org-d6sOkmC5UFSQEz57mmi0kpzM"
openai.api_key = "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"

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

# request

curl -X POST https://api.openai.com/v1/engines/davinci/completions \
    -H 'Content-Type: application/json' \
    

print("Done!")