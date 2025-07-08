# 📚 Smart Study Session Scheduler

This project is a simple AI-powered scheduling tool built with **Streamlit** and **n8n**.  
It lets users plan personalized study sessions for topics like **Machine Learning**, **Java**, or **Python**, and uses an AI agent to generate structured, realistic learning plans based on user conditions.

---

## 🚀 How It Works

✅ **Streamlit Frontend**  
- The user selects:
  - A subject (Machine Learning, Java, Python)
  - Specifies a topic they want to study
  - Picks a date & time
  - Adds any extra conditions (e.g., *“2 hours per day”*, *“Only weekends”*, *“I want 2 sessions”*)

✅ **n8n Backend**  
- The Streamlit app sends user input to an **n8n webhook**.
- n8n passes the data to an AI agent (OpenAI or Gemini) with a smart prompt that:
  - Checks for missing info
  - Automatically creates a structured plan
  - Adjusts the plan based on user conditions (like daily practice, multiple sessions, or preferred days)
- The plan is returned to Streamlit (or sent by email, saved to Google Calendar, etc.)

---

## 🧩 Project Structure

```plaintext
.
├── streamlit_app.py    # Main Streamlit app
├── README.md
└── (n8n workflow)      # Setup in your own n8n instance
