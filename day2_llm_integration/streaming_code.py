import requests
import json

# User input
user_prompt = input("Enter your prompt: ")

# Ollama API URL
url = "http://localhost:11434/api/chat"

# Request payload
payload = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    "stream": True
}

try:
    # Send request with streaming enabled
    response = requests.post(
        url,
        json=payload,
        stream=True
    )

    print("\nAI Response:\n")

    # Read streaming lines
    for line in response.iter_lines():

        if line:

            # Convert bytes to JSON
            data = json.loads(line)

            # Extract streamed text
            if "message" in data:
                content = data["message"]["content"]

                print(content, end="", flush=True)

except requests.exceptions.ConnectionError:
    print("\nConnection Error:")
    print("Make sure Ollama is running.")