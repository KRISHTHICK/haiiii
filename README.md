# 👗 SmartAI: AI-Powered Fashion & Personalization Platform

SmartAI is an advanced, modular AI application designed to revolutionize fashion recommendations, content creation, and outfit personalization using state-of-the-art computer vision and LLM technologies.

This project supports **both offline and online AI inference** using open-source models (e.g., Ollama), along with options for **paid models like OpenAI GPT-4 or Gemini Pro**. It also keeps users informed of each processing step with real-time status tracking.

## 🎯 Project Objectives

- Help users plan fashionable looks based on their wardrobe, event, and style preferences
- Enable fusion of trending fashion and traditional outfits with sustainable suggestions
- Work offline with local models (no internet required), and online with premium LLMs
- Guide users through the full process with clear task stage updates

---

## 🧩 Key Features

### 1️⃣ Offline Mode (Ollama & Device-Aware AI)
- Run selected tasks entirely offline using local LLMs and vision models
- Automatically switches to free/open-source models like TinyLLaMA or Mistral
- Internet-free inference for edge or prototype use

### 2️⃣ "Best in Me" Agent
> Personalized style + social media assistant
- Inputs: User's uploaded outfit, past poses, event description, optional prompt
- Outputs:
  - Suggested new trendy pose
  - Recommended outfit style
  - Auto-generated caption for social media

### 3️⃣ Trend + Tradition Fusion with Sustainable Suggestions
> Blend modern fashion trends with traditional elements
- Inputs: Trending style + user-selected tradition (e.g., saree, kurta)
- Output: Fusion outfit suggestion (visual + description)
- Option: Suggest eco-friendly/sustainable fashion alternatives for the same look

---

## ⚙️ Technology Stack

- **Frontend**: Streamlit (UI with dropdowns, status updates, image upload)
- **Backend**: Python (modular code for each feature)
- **AI Models**:
  - Free/Offline: Ollama (TinyLLaMA, Mistral, LLaVA)
  - Paid: OpenAI GPT-4, Gemini Pro, Claude 3 (optional toggle)
- **Vision Models**: ControlNet, BLIP, CLIP (as needed)
- **Status Tracking**: Real-time stage display (Uploading → Processing → Generating → Completed)

---

## 📦 Setup Instructions

```bash
# Pull models (optional)
ollama pull mistral
ollama pull tinyllama

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
