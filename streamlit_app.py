import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a model that is guaranteed to work everywhere
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Code Explainer & Debug Assistant")

code = st.text_area("Paste your code:", height=250)
language = st.selectbox("Language:", ["Python", "JavaScript", "C", "C++", "Java"])

if st.button("Analyze Code"):
    if not code.strip():
        st.error("Paste some code!")
    else:
        with st.spinner("Analyzing with Gemini..."):
            prompt = f"""
            Analyze this code and respond ONLY in JSON:

            Language: {language}
            Code:
            {code}

            JSON format:
            {{
                "explanation": "",
                "bugs": "",
                "optimized_code": "",
                "time_complexity": ""
            }}
            """

            response = model.generate_content(prompt)
            st.subheader("🔍 Result")
            st.write(response.text)
