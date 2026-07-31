from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Get user details
budget = input("Enter your budget with currency (Example: $50, £40, ₹500):\n")
food_type = input("Enter your food preference (Veg/Non-Veg):\n")
location = input("Enter your location:\n")

# Prompt Engineering
prompt = f"""
You are an international meal planning assistant.

Suggest meals based on the user's budget and location.

Rules:
1. Suggest meals within the given budget.
2. Use the currency provided by the user.
3. Consider local food availability and prices based on location.
4. Include meal name, ingredients, estimated cost, and reason.
5. Suggest affordable and healthy options.
6. Do not provide meals above the budget.

User Details:
Budget: {budget}
Food Preference: {food_type}
Location: {location}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

result = response.choices[0].message.content

print("\nSuggested Meals:")
print(result)