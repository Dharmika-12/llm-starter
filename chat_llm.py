import os
from dotenv import load_dotenv
from google import genai

# 1. Load the key from .env
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise SystemExit("GEMINI_API_KEY is missing. Check your .env file.")

# 2. Create the client and a chat session (the chat remembers earlier messages)
client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash-lite")

print("Chat started. Type 'quit' to exit.\n")

# 3. Keep asking until the user types quit
while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}\n")
    except Exception as error:
        print(f"\nSomething went wrong: {error}\n")