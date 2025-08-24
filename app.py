# # from transformers import pipeline
# import streamlit as st
# from google import genai
# import os
# from dotenv import load_dotenv
# from transformers import AutoTokenizer
# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")



# # @st.cache_resource
# # def sumarizer_model():
# #     return pipeline("summarization", model="t5-small")
# # summarizer = sumarizer_model()
#     # summary=summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

#     #task1
  
# st.title("Text Summarizer")
# st.write("Enter text below and get a summary.")

# text_input = st.text_area("Enter your text here", height=200)

# if st.button("Summarize"):
#     if text_input.strip():
      
#         client = genai.Client(api_key=api_key)

#         response = client.models.generate_content(
#             model="gemini-2.5-flash", contents=f"Summarize the following text: {text_input} "
#         )
#         print(response.text)
#         with st.container():
#             st.subheader("Summary:")
#             st.write(response.text)
#     else:
#         st.warning("Please enter some text to summarize.")





import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import os
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)   

st.title("Text Summarizer")
st.write("Upload a file OR type text below to summarize.")

uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
manual_text = st.text_area("Or write/paste text here", height=200)

text_input = ""


def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text


def read_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text_input = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text_input = read_docx(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(text_input[:1000] + "..." if len(text_input) > 1000 else text_input)
elif manual_text.strip():
    text_input = manual_text

summary = None

# Summarizer
if st.button("Summarize"):
    if text_input.strip():
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(f"Summarize the following text: {text_input}")
        summary = response.text

        with st.container():
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.warning("Please upload a file or write text to summarize.")

