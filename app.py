import streamlit as st
import pandas as pd

# پیج سیٹنگ
st.set_page_config(page_title="ACAG Search", layout="centered")

@st.cache_data
def load_data():
    # اس لائن کے شروع میں 4 اسپسز (Spaces) ہونا ضروری ہیں
    df = pd.read_csv('ACAG Portal Data.csv')
    df['ApplicantCNIC'] = df['ApplicantCNIC'].astype(str).str.strip()
    return df

# ہیڈنگ
st.markdown("<h2 style='text-align: center;'>ACAG ڈیٹا سرچ پورٹل</h2>", unsafe_allow_html=True)

try:
    df = load_data()
    
    search_query = st.text_input("اپنا شناختی کارڈ نمبر لکھیں (بغیر ڈیش کے):")

    if search_query:
        # سرچ کرنے کا عمل
        result = df[df['ApplicantCNIC'] == search_query.strip()]
        
        if not result.empty:
            st.success("ریکارڈ مل گیا ہے!")
            st.dataframe(result)
        else:
            st.error("معذرت، یہ ریکارڈ موجود نہیں ہے۔")

except Exception as e:
    st.error(f"فائل لوڈ کرنے میں مسئلہ ہے: {e}")
