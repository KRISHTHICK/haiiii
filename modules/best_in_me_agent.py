# CHATCODE#01

import streamlit as st

def best_in_me_ui():
    st.header("📸 Best in Me Agent")

    st.markdown("Upload your personal style elements for a personalized fashion suggestion.")

    # Model selection
    model_type = st.selectbox("Select LLM Model", ["Ollama (Free)", "GPT-4 (Paid)", "Gemini Pro (Paid)"])

    # Upload past poses
    pose_image = st.file_uploader("Upload one of your past poses", type=["jpg", "png", "jpeg"], key="pose")

    # Upload outfit image
    outfit_image = st.file_uploader("Upload your outfit image", type=["jpg", "png", "jpeg"], key="outfit")

    # Event
    event = st.text_input("Describe your event (e.g., wedding at Marriott rooftop)", key="event")

    # Optional prompt
    prompt = st.text_area("Optional prompt (e.g., suggest something elegant & trendy)", key="prompt")

    if st.button("Generate Suggestion"):
        st.session_state['status'] = "Reading Inputs..."
        st.success("Input captured. Move to next part.")
        return model_type, pose_image, outfit_image, event, prompt
    else:
        return None, None, None, None, None
