# app.py

import streamlit as st
from modules.best_in_me_agent import best_in_me_ui  # ✅ Correct way

st.set_page_config(page_title="SmartAI", layout="wide")

# Sidebar
with st.sidebar:
    st.header("🧭 Navigation")
    option = st.selectbox(
        "Choose a SmartAI Feature:",
        ("Best in Me Agent", "Option 2", "Option 3")
    )

# Main UI
st.title("👗 SmartAI – Fashion and Personalization Platform")

if option == "Best in Me Agent":
    best_in_me_ui()  # ✅ Call the function here
elif option == "Option 2":
    st.write("🧪 You are viewing content for Option 2.")
else:
    st.write("🧪 You are viewing content for Option 3.")
