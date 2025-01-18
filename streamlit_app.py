import streamlit as st
import re

# Title of the app
st.title("Advanced Treasure Hunting Assistant")

# Input Section
st.header("Input Your Clues or Chapter Text")
text_input = st.text_area("Paste your text or clues here:")
if text_input:
    st.write("---")

    # 1. Skim Overview
    st.subheader("Overview")
    titles = re.findall(r'\b(?:CHAPTER|TITLE|SECTION)\s+.*', text_input, re.IGNORECASE)
    st.write("Detected Titles or Sections:", titles)

    # 2. Extract Patterns and Themes
    st.subheader("Patterns & Themes")
    recurring_words = re.findall(r'\b\w+\b', text_input)
    word_frequency = {word: recurring_words.count(word) for word in set(recurring_words)}
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:10]
    st.write("Most Recurring Words:", sorted_words)

    # 3. Analyze Numbers & Codes
    st.subheader("Numbers & Codes")
    numbers = re.findall(r'\b\d+\b', text_input)
    alphanumeric_patterns = [chr(int(num)) for num in numbers if num.isdigit() and 65 <= int(num) <= 90]
    st.write("Numbers Found:", numbers)
    st.write("Potential Alphanumeric Decoding:", alphanumeric_patterns)

    # 4. Focus on Anomalies
    st.subheader("Anomalies")
    anomalies = [word for word in text_input.split() if len(word) > 10 or '-' in word]
    st.write("Unusual Words or Phrases:", anomalies)

    # 5. Cross-Referencing Information
    st.subheader("Cross-Referencing Information")
    # Dummy example for simplicity:
    if "California" in text_input and "moon" in text_input:
        st.write("Connection Detected: 'California' and 'moon' appear in the same context.")
    else:
        st.write("No direct references detected.")

    # 6. Map Physical References
    st.subheader("Physical References")
    place_keywords = ["mountain", "river", "lake", "city", "island", "ocean", "valley", "forest", "desert", "bay", "region"]
    geographic_references = [word for word in text_input.split() if any(kw in word.lower() for kw in place_keywords)]
    st.write("Geographic References Detected:", geographic_references)

    # 7. Hypothesis Testing (Optional)
    st.subheader("Hypotheses")
    st.write("Testing directional or time-related patterns...")
    if "sunrise" in text_input:
        st.write("Clue suggests time-related interpretation: Sunrise.")
    elif "steps" in text_input:
        st.write("Clue suggests movement: Look for steps or paths.")

    # 8. Document Findings
    st.write("---")
    st.download_button("Export Findings", data=f"{text_input}", file_name="treasure_analysis.txt")
else:
    st.warning("Please input some text to analyze!")