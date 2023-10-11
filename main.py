import openai
import os

# openai.api_key = process.env.APIKEY
openai.api_key = os.environ['APIKEY'] # Stored the API Key as a GitHub Actions Secret 

def AlisterGPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Welcome to AlisterGPT\nNote: Type 'bye', 'exit' or 'quit' to exit the app.\n")
    while True:
        inpuT = input("You: ")
        print()
        if inpuT.lower() in ["quit", "exit", "bye"]:
            break
        response = AlisterGPT(inpuT)
        print("AlisterGPT: ", response, "\n")

