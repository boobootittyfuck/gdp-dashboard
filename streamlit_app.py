# treasure_hunt_app.py

import streamlit as st

# Title of the app
st.title("Treasure Hunting Program")

# Input section
st.header("Input Your Text or Clue")
text_input = st.text_area("Paste your text or chapter here:")
if st.button("Analyze"):
    # Simple text analysis
    st.subheader("Analysis Results")
    
    # Recurring words
    words = text_input.split()
    word_count = {word: words.count(word) for word in set(words)}
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    st.write("Most Recurring Words:")
    st.write(sorted_word_count[:5])
    
    # Numbers in text
    import re
    numbers = re.findall(r'\d+', text_input)
    st.write("Numbers Found in Text:")
    st.write(numbers)
    
    # Anomalies
    st.write("Odd or Out-of-Place Details:")
    anomalies = [word for word in words if word.istitle() or word.isupper()]
    st.write(anomalies)