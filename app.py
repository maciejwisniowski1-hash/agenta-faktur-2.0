import streamlit as st
import pandas as pd
from pypdf import PdfReader
from io import BytesIO
import re

st.title("Agent Faktur v3")
st.write("Wgraj Excel i PDF")

excel=st.file_uploader("Excel",type=["xlsx"])
pdf=st.file_uploader("PDF",type=["pdf"])

if st.button("Analizuj") and excel and pdf:
    df=pd.read_excel(excel)
    text=""
    for p in PdfReader(pdf).pages:
        t=p.extract_text()
        if t: text+=t+"\n"
    st.success(f"Odczytano {len(df)} rekordów faktur")
    st.download_button("Pobierz tekst PDF", text, file_name="pdf.txt")
