import streamlit as st
import whisper

st.title("🎧 Speech Transcription App (Line-by-Line)")

# Cache the model so it loads only once
@st.cache_resource
def load_model():
    return whisper.load_model("medium")

model = load_model()  # This will only load once

uploaded_file = st.file_uploader("Upload an audio file (.mp3 or .wav)", type=["mp3", "wav"])

if uploaded_file:
    input_path = f"uploaded.{uploaded_file.name.split('.')[-1]}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded!")

    # Audio playback
    st.audio(input_path, format='audio/wav')
    st.caption("🎵 Listen to the uploaded audio")

    st.info("Transcribing audio line by line...")
    result = model.transcribe(input_path)

    st.subheader("📝 Line-by-Line Transcription")
    for segment in result["segments"]:
        text = segment["text"].strip()
        st.write(f" {text}")
