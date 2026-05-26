import requests

url = "http://localhost:11434/api/chat"

# Reusable function to call Ollama
def ask_llm(prompt):
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()

    # Safe extraction
    if "message" in data:
        return data["message"]["content"]
    else:
        return str(data)


# Input text
text = """
Artificial Intelligence is transforming the world.
It is used in healthcare, finance, education, and automation.
"""

# STEP 1: Summarize
summary = ask_llm(f"Summarize this text:\n{text}")
print("\n--- SUMMARY ---\n")
print(summary)

# STEP 2: Extract keywords
keywords = ask_llm(f"Extract 5 keywords from:\n{summary}")
print("\n--- KEYWORDS ---\n")
print(keywords)

# STEP 3: Final output (Report)
final_output = ask_llm(f"""
Using this summary and keywords, write a short professional report.

Summary:
{summary}

Keywords:
{keywords}
""")

print("\n--- FINAL REPORT ---\n")
print(final_output)