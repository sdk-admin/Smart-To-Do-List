import streamlit as st
import google.generativeai as genai
import requests

# -------------------------------
# CONFIGURE GEMINI
# -------------------------------
# Replace this with your own API key!
genai.configure(api_key="AIzaSyDk7k-euWZXXRR58UVOs_wGIJe3aYpEGS4")

# Create the Gemini model once
model = genai.GenerativeModel("gemini-2.0-flash")

# -------------------------------
# CONFIGURE YOUR N8N WEBHOOK URL
# -------------------------------
WEBHOOK_URL = "https://smartdrive-ai.app.n8n.cloud/webhook-test/task"
# 👉 Replace with your real webhook URL!


# -------------------------------
# Streamlit App
# -------------------------------

st.title("📝 Smart To-Do List with Gemini AI & n8n Webhook")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "suggestions" not in st.session_state:
    st.session_state.suggestions = []

# Function to send data to n8n webhook
def send_to_webhook(task, suggestion):
    payload = {
        "task": task,
        "suggestion": suggestion
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            st.success("✅ Sent to n8n webhook!")
        else:
            st.error(f"❌ Failed to send to webhook. Status: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error sending to webhook: {e}")

# Add task input
task_input = st.text_input("Add a new task:")

if st.button("Add Task"):
    if task_input.strip() != "":
        st.session_state.tasks.append(task_input.strip())

        # Get Gemini AI suggestion
        prompt = f"Give me one short productivity tip for completing this task: '{task_input.strip()}'"
        response = model.generate_content(prompt)
        suggestion = response.text.strip()

        st.session_state.suggestions.append(suggestion)

        # Send to n8n webhook
        send_to_webhook(task_input.strip(), suggestion)

# Display tasks with Gemini suggestions
st.subheader("Your Tasks:")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"✅ {task}")
        st.caption(f"Gemini Suggestion: {st.session_state.suggestions[i]}")
else:
    st.write("No tasks added yet. Add your first task above! 🎯")
