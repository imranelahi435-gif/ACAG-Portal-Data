import streamlit as st
import pandas as pd

st.set_page_config(page_title="ACAG Search", layout="wide")

@st.cache_data
def load_data():
    # فائل کا نام بالکل صحیح ہونا چاہیے
    df = pd.read_csv('ACAG Portal Data.csv')
    # CNIC کو ٹیکسٹ میں بدلیں تاکہ سرچ ہو سکے
    df['ApplicantCNIC'] = df['ApplicantCNIC'].astype(str).str.strip()
    return df

st.title("🔎 ACAG پورٹل ڈیٹا سرچ")

try:
    df = load_data()
    search = st.text_input("شناختی کارڈ نمبر (CNIC) لکھیں:")

    if search:
        # یہاں ہم چیک کر رہے ہیں کہ کیا نمبر موجود ہے
        result = df[df['ApplicantCNIC'] == search.strip()]
        
        if not result.empty:
            st.success("ریکارڈ مل گیا ہے!")
            st.dataframe(result)
        else:
            st.error("معذرت، یہ CNIC ریکارڈ میں موجود نہیں ہے۔")

except Exception as e:
    st.error(f"ایرر: {e}")
