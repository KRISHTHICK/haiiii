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

# CHATCODE#02

import time
import base64
from components.status_tracker import show_stage

def generate_caption_and_pose(pose_image, outfit_image, event, prompt, model_type):
    show_stage("Reading Images and Inputs...")

    # Simulate image conversion (mocked for now)
    time.sleep(1)
    pose_str = f"[User Pose Uploaded]"
    outfit_str = f"[Outfit Image Uploaded]"

    # Format prompt
    full_prompt = f"""
You are an AI fashion stylist.
User is attending: {event}.
They uploaded a pose: {pose_str}
They uploaded an outfit: {outfit_str}
User says: {prompt if prompt else 'No extra prompt'}.
Suggest:
1. A new trendy pose
2. A fitting outfit suggestion
3. Caption for social media
    """

    show_stage("Generating Output...")

    # Free LLM Option (Simulate)
    if "Ollama" in model_type:
        mock_response = """
🧍‍♀️ Pose: Hand-on-hip with a side glance  
👗 Outfit Suggestion: Elegant Indo-Western gown with minimal jewelry  
✍️ Caption: "Owning the spotlight, one twirl at a time ✨"
        """
        result = mock_response

    # Paid LLM (Simulate for now)
    else:
        mock_response = """
🧍‍♀️ Pose: Lean against the railing, head tilted  
👗 Outfit Suggestion: Satin maroon drape dress with metallic heels  
✍️ Caption: "When elegance meets rooftop dreams 🌆"
        """
        result = mock_response

    show_stage("Completed ✅")

    st.subheader("✨ Your Personalized Suggestion")
    st.code(result, language='markdown')

