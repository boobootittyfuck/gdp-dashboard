import streamlit as st
import re

# Title of the app
st.title("Treasure Hunting Program")

# Input section
st.header("Input Your Text or Clue")
text_input = st.text_area("Paste your text or chapter here:")

if st.button("Analyze"):
    if text_input:
        # Simple text analysis
        st.subheader("Analysis Results")

        # Recurring words
        words = text_input.split()
        word_count = {word: words.count(word) for word in set(words)}
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        st.write("Most Recurring Words:")
        st.write(sorted_word_count[:5])

        # Numbers in the text
        numbers = re.findall(r'\b\d+\b', text_input)
        st.write("Numbers Found in Text:")
        st.write(numbers)

        # Odd or out-of-place details
        anomalies = [word for word in words if len(word) > 10]
        st.write("Odd or Out-of-Place Words:")
        st.write(anomalies)

        # Find potential dates
        years = [number for number in numbers if 1000 <= int(number) <= 2100]
        st.write("Potential Years Found:")
        st.write(years)

        # Analyze for capitalized words or phrases
        capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text_input)
        st.write("Capitalized Words or Phrases:")
        st.write(capitalized_words)

    else:
        st.warning("Please provide some text to analyze!")