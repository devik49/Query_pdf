import PyPDF2
import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

def text_extracter(file_path):

    pdf_reader = PyPDF2.PdfReader(file_path)
    text = ''
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text += page.extract_text()
    return text
 
def model(full_text,user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f""" 
    given sentence : {full_text}
    """
    response = model.generate_content([prompt,user_input])
    return response.text

def streamlit_main():
    uploaded_file = st.file_uploader("file upload",type="pdf")
    data = text_extracter(uploaded_file)
    user_input = st.text_input("ASK question :")
    if user_input:
        response = model(data,user_input)    
        st.write(response)   

if __name__ == '__main__':
    streamlit_main()
    









    