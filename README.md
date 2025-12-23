# Med-SOAP Transformer 🩺

Detta projekt demonstrerar hur man kan använda moderna språkmodeller (LLMs) för att automatiskt generera strukturerade journalanteckningar enligt SOAP-standarden från patientmöten. 

**Inspiration:** Tandem Healths arbete med att minska vårdpersonalens administrativa börda.

## Varför detta projekt?
Att manuellt skriva journaler tar värdefull tid från patientkontakten. Genom att använda **Llama 3 via Groq**, visar detta verktyg hur vi kan:
1. **Automatisera struktur:** Omvandla naturligt tal till S, O, A och P-sektioner.
2. **Säkerställa hastighet:** Använder Groqs LPU-teknologi för att generera anteckningar på under 1 sekund.
3. **Öka flexibiliteten:** Genom att använda Open Source-modeller (Llama) istället för låsta system, kan man i framtiden köra lösningen i säkrare, lokala miljöer (on-premise).

## Teknikstack
- **Språk:** Python
- **Gränssnitt:** Streamlit
- **Motor:** Llama-3.3-70B via Groq Cloud API
- **Miljö:** Miljövariabler via `.env` för säker hantering av API-nycklar.

## Hur man testar
1. Klona repot.
2. Installera krav: `pip install -r requirements.txt`.
3. Lägg till din Groq API-nyckel i `.env`.
4. Kör `streamlit run main.py`.

---
*Ansvarsfriskrivning: Detta är ett utbildningsprojekt. Ingen riktig patientdata har använts eller bör användas i denna demo.*# SoapEngine
