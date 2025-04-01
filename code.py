import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")  # Store API key in Streamlit secrets

def convert_cobol_to_java(cobol_code):
    """Uses an LLM to convert COBOL to Java."""
    prompt = f"""
    Convert the following COBOL code to Java while keeping the same functionality:
    
    {cobol_code}
    
    Ensure that:
    1. The Java code follows modern best practices.
    2. Equivalent logic is maintained.
    3. Provide comments for better understanding.
    """
    llm = ChatGroq(api_key=groq_api_key, model="llama3-70b-8192")
    response = llm.invoke(prompt)
    return response.content

# Streamlit UI
st.title("COBOL to Java Converter 💻")
st.write("Upload a COBOL file and convert it to Java using Generative AI.")

uploaded_file = st.file_uploader("Upload COBOL File", type=["cobol", "txt"])

if uploaded_file is not None:
    cobol_code = uploaded_file.read().decode("utf-8")
    st.subheader("📜 COBOL Code:")
    st.text_area("", cobol_code, height=200)
    
    if st.button("Convert to Java 🚀"):
        with st.spinner("Converting... Please wait."):
            java_code = convert_cobol_to_java(cobol_code)
            st.subheader("✅ Converted Java Code:")
            st.code(java_code, language="java")
            
            # Save converted Java code for download
            java_filename = "ConvertedCode.java"
            with open(java_filename, "w", encoding="utf-8") as f:
                f.write(java_code)
                
            st.download_button("📥 Download Java Code", java_code, file_name=java_filename, mime="text/plain")
