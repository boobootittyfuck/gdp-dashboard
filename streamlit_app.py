# treasure_hunt_app.py

import streamlit as st
import re

# Title of the app
st.title("Advanced Treasure Hunting Program")

# Input section
st.header("Input Your Text or Clue")
text_input = st.text_area("Paste your text or chapter here:")

if st.button("Analyze"):
    if text_input.strip():
        st.subheader("Analysis Results")

        # 1. Chapter Titles & Subtitles
        chapter_titles = re.findall(r'(CHAPTER [A-Z]+|[A-Z][a-z]+ [A-Z][a-z]+)', text_input)
        st.write("Extracted Chapter Titles & Subtitles:")
        st.write(chapter_titles)

        # 2. Recurring Words & Patterns
        words = text_input.split()
        word_count = {word: words.count(word) for word in set(words)}
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        st.write("Most Recurring Words:")
        st.write(sorted_word_count[:10])

        # 3. Numbers and Codes
        numbers = re.findall(r'\b\d+\b', text_input)
        st.write("Numbers Found in Text:")
        st.write(numbers)

        # Alphanumeric Decoding
        alphanumeric_decoding = [chr(96 + int(n)) for n in numbers if n.isdigit() and 1 <= int(n) <= 26]
        st.write("Potential Alphanumeric Decoding:")
        st.write(alphanumeric_decoding)

        # 4. Focus on Anomalies
        # Italicized or quoted text
        anomalies = re.findall(r'"(.*?)"|‘(.*?)’|“(.*?)”', text_input)
        anomalies_flat = [item for sublist in anomalies for item in sublist if item]
        st.write("Unusual Words or Phrases:")
        st.write(anomalies_flat)

        # 5. Cross-Referencing Information
        cross_references = []
        for word in ['moon', 'California']:
            if word in text_input:
                cross_references.append(word)
        st.write("Cross-Referencing Information:")
        if cross_references:
            st.write(f"Connection Detected: {' and '.join(cross_references)} appear in the same context.")
        else:
            st.write("No meaningful cross-references detected.")

        # 6. Map Out Physical References
        geographic_references = re.findall(r'(California|mountain|river|bay|ocean)', text_input, re.IGNORECASE)
        st.write("Geographic References Detected:")
        st.write(list(set(geographic_references)))

        # 7. Hypotheses
        st.write("Hypotheses:")
        if "step" in text_input.lower():
            st.write("Clue suggests movement: Look for steps or paths.")
        if "moon" in text_input.lower():
            st.write("Could the 'moon' reference relate to a lunar feature or shape?")
        if "California" in text_input.lower():
            st.write("Consider exploring locations in California.")

        # 8. Export Findings
        st.download_button("Export Findings", data=text_input, file_name="treasure_hunt_analysis.txt")

    else:
        st.warning("Please provide text to analyze!")