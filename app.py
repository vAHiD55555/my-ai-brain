import streamlit as st
import google.generativeai as genai

# تنظیمات کلید از محیط امن استریم‌لیت
GOOGLE_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_KEY)

def get_free_response(prompt, system_instruction):
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)
    response = model.generate_content(prompt)
    return response.text

st.title("🤖 Free AI Brainstorming Team")

user_input = st.text_area("Product concept:")

if st.button("Consult"):
    with st.status("Agent 1 (Brainstorming)..."):
        idea = get_free_response(user_input, "You are a creative product manager.")
    
    with st.status("Agent 2 (Critique)..."):
        critique = get_free_response(idea, "You are a strict technical critic. Find flaws in the idea.")
        
    st.write("### Idea:", idea)
    st.write("### Critique:", critique)
