# Make me a streamlit app that has a text input and a button. When the button is clicked, it should display the text that was entered in the text input.
import streamlit as st
def main():
    st.title("Text Display App")
    user_input = st.text_input("Enter some text:")
    if st.button("Display Text"):
        st.write(f"You entered: {user_input}")
if __name__ == "__main__":    main()
