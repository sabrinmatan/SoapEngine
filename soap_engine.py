import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class SOAPTransformer:
    def __init__(self, api_key):
        # Initierar Groq-klienten med din API-nyckel
        self.client = Groq(api_key=api_key)

    def transcribe_audio(self, audio_file):
        """Omvandlar ljud till text med Whisper-v3."""
        try:
            # Whisper-large-v3 är optimerad för medicinska termer och olika accenter
            transcription = self.client.audio.transcriptions.create(
                file=(audio_file.name, audio_file.read()),
                model="whisper-large-v3",
                response_format="text",
                language="sv"  # Tvingar modellen att fokusera på svenska
            )
            return transcription
        except Exception as e:
            return f"Transkriberingsfel: {str(e)}"

    def generate_soap_note(self, transcript):
        """Strukturerar text till SOAP-format med Llama-3.3."""
        system_prompt = """
        Du är en expert på medicinsk dokumentation. Din uppgift är att transformera en dialog mellan 
        en läkare och en patient till en formell SOAP-anteckning på SVENSKA.

        Följ dessa strikta regler:
        1. S (Subjective): Patientens egna upplevelser, symptom och historik.
        2. O (Objective): Mätbara data, observationer och fynd från undersökningen.
        3. A (Assessment): Preliminär diagnos eller bedömning av tillståndet.
        4. P (Plan): Nästa steg, behandling, medicinering eller uppföljning.

        VIKTIGT: 
        - Lägg INTE till information som inte finns i transkriptet (ingen hallucination).
        - Behåll en professionell, klinisk ton.
        - Om information saknas för en sektion, skriv 'Ej diskuterat'.
        """

        try:
            # Vi använder Llama-3.3-70b för högsta precision i analysen
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Här är transkriptet:\n\n{transcript}"}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ett fel uppstod vid generering: {str(e)}"