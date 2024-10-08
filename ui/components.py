import streamlit as st



def upload_resume():
    return st.file_uploader("Choose a resume file", type=["txt", "pdf", "docx", "doc"])

def display_applicants(applicants):
    st.subheader("Applicants")
    st.dataframe(applicants)

def search_interface(search_function):
    search_term = st.text_input("Search resumes:")
    if search_term:
        results = search_function(search_term)
        st.dataframe(results)