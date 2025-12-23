import streamlit as st
from soap_engine import SOAPTransformer

# Sidkonfiguration
st.set_page_config(page_title="Med-SOAP AI", page_icon="🩺", layout="wide")

st.title("🩺 Med-SOAP: Från samtal till journal")
st.markdown("---")

# Sidebar för inställningar
with st.sidebar:
    st.header("Konfiguration")
    api_key = st.text_input("Groq API Key", type="password", help="Hämta din nyckel på console.groq.com")
    st.info("Denna demo använder Whisper-v3 för ljud och Llama-3.3 för medicinsk logik via Groq.")

# Skapar flikar för olika input-metoder
tab1, tab2 = st.tabs(["🎙️ Ljuduppladdning (Ambient)", "⌨️ Manuell text"])

transformer = None
if api_key:
    transformer = SOAPTransformer(api_key)

with tab1:
    st.subheader("Ladda upp patientsamtal")
    audio_file = st.file_uploader("Välj en ljudfil (mp3, wav, m4a)", type=['mp3', 'wav', 'm4a'])

    if audio_file and transformer:
        if st.button("Transkribera och generera anteckning"):
            with st.spinner("AI:n lyssnar igenom samtalet..."):
                # Steg 1: Transkribering
                transcript = transformer.transcribe_audio(audio_file)
                st.write("**Identifierad dialog:**")
                st.info(transcript)

                # Steg 2: SOAP-generering
                with st.spinner("Strukturerar kliniska data..."):
                    soap_result = transformer.generate_soap_note(transcript)
                    st.success("Klar! Här är din SOAP-anteckning:")
                    st.markdown(soap_result)
                    st.download_button("Spara anteckning", soap_result, file_name="journal.txt")

with tab2:
    st.subheader("Klistra in dialog manuellt")
    text_input = st.text_area("Skriv eller klistra in samtalet här:", height=200)

    if st.button("Generera från text") and transformer:
        if text_input:
            with st.spinner("Analyserar text..."):
                soap_result = transformer.generate_soap_note(text_input)
                st.markdown(soap_result)
        else:
            st.warning("Vänligen skriv in lite text först.")

# Fotnot
st.markdown("---")
st.caption("Studentprojekt inspirerat av Tandem Health. All data behandlas via Groq Cloud API.")