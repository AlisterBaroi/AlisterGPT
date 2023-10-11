import openai
import os

openai.api_key = process.env.APIKEY

def AlisterGPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        print("Welcome to AlisterGPT\nNote: Type 'bye', 'exit' or 'quit' to exit the app.")
        inpuT = input("You: ")
        if inpuT.lower() in ["quit", "exit", "bye"]:
            break
        response = AlisterGPT(inpuT)
        print("AlisterGPT: ", response)

