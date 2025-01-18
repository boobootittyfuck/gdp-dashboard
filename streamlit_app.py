# Import required libraries
import streamlit as st
from PIL import Image
import pytesseract
import re
from collections import Counter

# Set the title of the app
st.title("Treasure Hunting Program")

# Input section
st.header("Input Your Text, Clue, or Image")

# Add a file uploader for images
uploaded_file = st.file_uploader("Upload an image of a clue (optional)", type=["png", "jpg", "jpeg"])

# Add a text area for inputting text
text_input = st.text_area("Paste your text or chapter here:")

# Button to analyze
if st.button("Analyze"):
    st.subheader("Analysis Results")

    # If an image is uploaded, extract text from the image
    if uploaded_file:
        image = Image.open(uploaded_file)
        extracted_text = pytesseract.image_to_string(image)
        st.write("Extracted Text from Image:")
        st.write(extracted_text)
        text_input += " " + extracted_text  # Combine image text with user text

    # Analyze text input (if any)
    if text_input.strip():
        # Extract recurring words
        words = re.findall(r'\b\w+\b', text_input.lower())
        word_counts = Counter(words)
        sorted_word_counts = word_counts.most_common(10)

        st.write("Most Recurring Words:")
        st.write(sorted_word_counts)

        # Extract numbers
        numbers = re.findall(r'\b\d+\b', text_input)
        st.write("Numbers Found in Text:")
        st.write(numbers)

        # Highlight odd or out-of-place words
        anomalies = [word for word, count in word_counts.items() if len(word) > 6 and count == 1]
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
        st.warning("Please provide either an image or text to analyze!")