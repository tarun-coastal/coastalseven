import requests

# Ask user for prompt
user_prompt = input("Enter your prompt: ")

# Ollama API endpoint
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
    "stream": False
}

# Send request
response = requests.post(url, json=payload)

# Convert response to JSON
data = response.json()

# Print AI response
print("\nAI Response:\n")
print(data["message"]["content"])