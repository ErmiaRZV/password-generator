import streamlit as st
import nltk
from main import pinGenerator, memorablePasswordGenerator, randomPasswordGenerator
nltk.download('words')
st.title("Password Generator")
st.write('developed by   Ermia Razavi')

# Radio buttons to select password type
password_type = st.radio(
    "Select Password Type", 
    ('PIN', 'Memorable Password', 'Random Password')
)

# Configure generator based on selection
if password_type == 'PIN':
    length = st.number_input("Enter PIN Length", min_value=4, max_value=50, value=4)
    generate = pinGenerator(length)

elif password_type == 'Memorable Password':
    number_of_words = st.number_input("Enter Number of Words", min_value=4, max_value=50, value=4)
    include_upper = st.checkbox("Include Uppercase Letters")
    separator = st.text_input("Enter Separator", value="-")
    generate = memorablePasswordGenerator(number_of_words, include_upper, separator)

elif password_type == 'Random Password':
    length = st.number_input("Enter Password Length", min_value=4, max_value=50, value=4)
    include_digits = st.checkbox("Include Digits")
    include_symbols = st.checkbox("Include Symbols")
    include_capitals = st.checkbox("Include Capital Letters")
    generate = randomPasswordGenerator(length, include_digits, include_symbols, include_capitals)

# Generate password button
if st.button("Generate Password"):
    st.success(f"Your password is: {generate.generate_password()}")
