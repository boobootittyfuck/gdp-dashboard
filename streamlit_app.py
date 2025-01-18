import re
import streamlit as st
from collections import Counter

# Title of the app
st.title("Advanced Treasure Hunting Assistant")

# Input section
st.header("Input Your Text or Clue")
text_input = st.text_area("Paste your text or chapter here:")

if st.button("Analyze"):
    if text_input.strip():
        st.subheader("Analysis Results")

        # 1. Overview and Detailed Reading
        st.markdown("### Overview and Detailed Reading")
        chapters = re.findall(r"(Chapter [A-Z]+: [^\n]+)", text_input, re.IGNORECASE)
        highlights = re.findall(r"\*\*([^\*]+)\*\*", text_input)
        st.write("**Chapters Found:**", chapters if chapters else "None found")
        st.write("**Highlighted Sections:**", highlights if highlights else "None found")

        # 2. Patterns and Themes
        st.markdown("### Patterns and Themes")
        recurring_phrases = Counter(re.findall(r'\b\w+\b', text_input.lower()))
        common_words = [word for word, count in recurring_phrases.most_common(20) if len(word) > 3]
        st.write("Most Common Words/Phrases:", common_words)

        # 3. Numbers and Codes
        st.markdown("### Numbers and Codes")
        numbers = re.findall(r"\b\d+\b", text_input)
        st.write("Numbers Found:", numbers)

        alphanumeric = re.findall(r"\b[A-Za-z0-9]+\b", text_input)
        st.write("Potential Alphanumeric Codes:", alphanumeric)

        # 4. Focus on Anomalies
        st.markdown("### Anomalies")
        odd_words = re.findall(r"[A-Z][a-z]+|[\*\_\-]", text_input)
        st.write("Unusual Words or Phrases:", odd_words)

        # 5. Cross-Referencing Information
        st.markdown("### Cross-Referencing Information")
        locations = re.findall(r"\b[A-Z][a-z]+\b", text_input)
        connections = set()
        if "California" in locations and "moon" in locations:
            connections.add("California and moon appear in the same context.")
        st.write("Connections Detected:", list(connections) if connections else "None")

        # 6. Map Out Physical References
        st.markdown("### Physical References")
        landmarks = re.findall(r"\b(Mountain|River|Lake|Forest|Valley)\b", text_input, re.IGNORECASE)
        st.write("Geographic References Detected:", landmarks)

        # 7. Hypotheses
        st.markdown("### Hypotheses")
        if "steps" in text_input.lower() or "path" in text_input.lower():
            st.write("Clue suggests movement: Look for steps or paths.")
        if "moon" in text_input.lower():
            st.write("Could the 'moon' reference relate to a lunar feature or shape?")

        # 8. Research Context
        st.markdown("### Research Suggestions")
        st.write("Consider looking into cultural or historical references mentioned.")

        # 10. Document Everything
        st.markdown("### Export Findings")
        findings = {
            "Chapters": chapters,
            "Highlights": highlights,
            "Common Words": common_words,
            "Numbers": numbers,
            "Alphanumeric Codes": alphanumeric,
            "Anomalies": odd_words,
            "Connections": list(connections),
            "Geographic References": landmarks,
        }
        st.download_button("Export Findings", data=str(findings), file_name="findings.txt")
    else:
        st.warning("Please provide some text to analyze!")