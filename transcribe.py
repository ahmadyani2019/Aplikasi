# Modul yang digunakan ------------------------------------------------------------

from email.mime import audio
import streamlit as st
import requests
import speech_recognition as sr

# Judul program ------------------------------------------------------------

st.set_page_config(
    page_title="Audio and Video Transciption", page_icon="📃", layout="wide"
)

st.markdown(
    '# 📝 **Audio and Video Transciption oleh Ahmad Yani (11190910000004)**')
bar = st.progress(0)

# Layout interface program -------------------------------------------------


def _max_width_():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


_max_width_()

# Membuat dua menu untuk Audio dan Video -------------------------------------------------


def main():
    pages = {
        "🔉 Audio Transcription": audiot,
        # "📽️ Video Transcriber": videot,

    }

    if "page" not in st.session_state:
        st.session_state.update(
            {
                # Default page
                "page": "Home",
            }
        )

    with st.sidebar:
        page = st.radio("Pilih model AI", tuple(pages.keys()))

    pages[page]()

# Bagian Audio Transcription -------------------------------------------------


def audiot():

    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:

        with st.form(key="my_form"):

            uploaded_file = st.file_uploader("Unggah rekaman", type=[".wav"])
            st.info(
                f"""
                    👆 Hanya dapat membaca format .wav
                     """
            )

            submit_button = st.form_submit_button(label="Transcript")

    if uploaded_file is not None:
        r = sr.Recognizer()
        with sr.AudioFile(uploaded_file) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language="id-ID")
            st.success(print("Transkrip: {}".format(text)))

            c0, c1 = st.columns([2, 2])

            with c0:
                st.download_button(
                    "Download the transcription",
                    text,
                    file_name=None,
                    mime=None,
                    key=None,
                    help=None,
                    on_click=None,
                    args=None,
                    kwargs=None,
                )

        except sr.UnknownValueError:
            print(
                "Google Speech Recognition tidak bisa mengerti suara dalam file tersebut.")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        st.warning(
            "🚨 Mohon maaf, file audio tidak dapat diproses."
        )
        st.stop()
