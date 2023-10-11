import openai
openai.api_key = "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"

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

