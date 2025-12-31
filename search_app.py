import streamlit as st
import pandas as pd

"st.set_page_config(page_title=""CNIC Batch Finder"", layout=""centered"")"

@st.cache_data
def load_data():
    # Load the CSV file
    df = pd.read_csv('ACAG Portal Data.csv')
    # Convert CNIC to string for easier searching
    df['ApplicantCNIC'] = df['ApplicantCNIC'].astype(str)
    return df

"st.title(""ACAG Batch Finder"")"
"st.write(""Enter a CNIC to find the Batch Number."")"

df = load_data()

"search_query = st.text_input(""Enter CNIC (without dashes):"")"

if search_query:
    result = df[df['ApplicantCNIC'].str.contains(search_query)]
    
    if not result.empty:
"        st.success(f""Found {len(result)} record(s):"")"
"        st.dataframe(result[['ApplicantCNIC', 'ApplicantName', 'Batch No.']])"
    else:
"        st.error(""No record found for this CNIC."")"

"st.info(f""Total Database Records: {len(df):,}"")"
