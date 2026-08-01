from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("=" * 60)
print("🍽️ AI Meal Budget Assistant")
print("Type 'exit' to quit.")
print("=" * 60)

# System Prompt (Prompt Engineering)
messages = [
    {
        "role": "system",
        "content": """
You are an expert meal planning assistant.

Your responsibilities:
- Suggest meals within the user's budget.
- Consider location, food preference, and meal type.
- Recommend healthy alternatives.
- Estimate meal costs.
- Remember previous conversation and use it for future responses.
- If the user changes the budget or location, update your suggestions.
- Be friendly and conversational.
"""
    }
]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\n👋 Thank you for using the AI Meal Budget Assistant!")
        break

    # Store user message (Context Engineering)
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=700
    )

    assistant_reply = response.choices[0].message.content

    print("\nAssistant:", assistant_reply)

    # Save assistant reply so it remembers the conversation
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )
