# 🍽️ AI Meal Planner Assistant using Groq LLM 🤖

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Prompt%20Engineering-AI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/API-Powered-purple?style=for-the-badge">
</p>

---

## 🌟 Project Overview

**AI Meal Planner Assistant** is an intelligent meal recommendation system powered by **Groq LLM** and **Prompt Engineering**.

The application takes user inputs like:

💰 Budget  
🥗 Food Preference (Veg / Non-Veg)  
📍 Location  

and generates affordable, healthy, and location-based meal suggestions.

The AI assistant considers the user's budget and provides:

✅ Meal Name  
✅ Ingredients  
✅ Estimated Cost  
✅ Reason for Recommendation  
✅ Healthy & Affordable Options  

---

# 🚀 Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Powered | Uses Groq Large Language Model |
| 💰 Budget Based Planning | Suggests meals within user budget |
| 🌍 Location Awareness | Considers local food availability |
| 🥗 Food Preferences | Supports Veg and Non-Veg choices |
| 📝 Prompt Engineering | Uses structured AI instructions |
| ⚡ Fast Response | Powered by Groq API |

---

# 🏗️ Project Architecture

```
              User Input
                  |
                  |
        --------------------
        |                  |
      Budget          Food Preference
        |                  |
        |              Location
        |
        ↓
  Prompt Engineering
        |
        ↓
   Groq LLM API
        |
        ↓
 AI Meal Recommendation
        |
        ↓
   Suggested Meals
```

---

# 🛠️ Technologies Used

<div>

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🔥 Groq API | Large Language Model |
| 🌱 python-dotenv | Environment Variable Management |
| 🧠 Prompt Engineering | AI Response Optimization |
| 🤖 Llama 3.3 70B | AI Model |

</div>

---

# 📂 Project Structure

```
AI-Meal-Planner/
│
├── main.py
├── .env
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Meal-Planner.git
```

## 2️⃣ Navigate Project Folder

```bash
cd AI-Meal-Planner
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Required Libraries

```bash
pip install groq python-dotenv
```

---

# 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Replace:

```
your_api_key_here
```

with your actual Groq API key.

---

# ▶️ Run Application

Execute:

```bash
python main.py
```

---

# 💻 Example Execution

```
Enter your budget with currency:
₹500

Enter your food preference:
Veg

Enter your location:
Hyderabad
```

### 🤖 AI Output:

```
Suggested Meals:

🍛 Vegetable Biryani
Ingredients:
- Rice
- Vegetables
- Spices

Estimated Cost:
₹120

Reason:
Affordable and nutritious local meal option.
```

---

# 🧠 Prompt Engineering Approach

The AI prompt contains clear instructions:

```
You are an international meal planning assistant.

Rules:
1. Suggest meals within budget.
2. Use provided currency.
3. Consider local availability.
4. Provide ingredients and estimated cost.
5. Recommend healthy options.
```

This improves:

✨ Accuracy  
✨ Relevance  
✨ Structured Responses  
✨ User Experience  

---

# 🔮 Future Enhancements

🚀 Add Web Interface using FastAPI  
🚀 Add Food Nutrition Information  
🚀 Add Restaurant Recommendations  
🚀 Add Image-Based Food Recognition  
🚀 Add User History and Preferences  
🚀 Deploy using Cloud Platforms  

---

# 🎯 Learning Outcomes

Through this project, I learned:

✅ Integrating LLM APIs with Python  
✅ Using Groq API for AI applications  
✅ Writing effective prompts  
✅ Managing API keys securely  
✅ Building AI-powered recommendation systems  

---

# 👨‍💻 Author

**Jonnadula Naga Samba Siva Rao**

⭐ AI | Python | LLM | Prompt Engineering Enthusiast

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub!

Happy Coding 🚀
