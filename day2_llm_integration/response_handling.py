import requests

# Take input from terminal
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
    "stream": False
}

try:
    # Send POST request
    response = requests.post(url, json=payload)

    # Check HTTP status code
    if response.status_code == 200:

        # Convert response to JSON
        data = response.json()

        # Check if 'message' exists
        if "message" in data:

            # Extract AI response
            ai_response = data["message"]["content"]

            print("\nAI Response:\n")
            print(ai_response)

        else:
            print("\nError: 'message' key not found")
            print(data)

    else:
        print(f"\nHTTP Error: {response.status_code}")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("\nConnection Error:")
    print("Make sure Ollama is running.")

except requests.exceptions.Timeout:
    print("\nRequest Timeout")

except requests.exceptions.RequestException as e:
    print("\nRequest Failed:")
    print(e)