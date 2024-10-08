import streamlit as st
from ui.components import upload_resume, display_applicants, search_interface
from resume_processing.parser import parse_resume
from resume_processing.scorer import score_resume
from data.storage import add_applicant, get_applicants, search_applicants

def try_decode(file_content):
    encodings = ['utf-8', 'iso-8859-1', 'windows-1252', 'ascii']
    for encoding in encodings:
        try:
            return file_content.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None

from utils.file_handler import read_file_content

# ... (previous imports)

def run_app():
    st.title("Advanced ATS System")

    uploaded_file = upload_resume()

    if uploaded_file:
        file_content = read_file_content(uploaded_file)
        content = try_decode(file_content) if isinstance(file_content, bytes) else file_content
        
        if content is None:
            st.error("Unable to read the file. Please ensure it's a valid resume file.")
            return

        # ... (rest of the function remains the same)
        with st.spinner('Parsing resume... This may take a moment.'):
            parsed_info = parse_resume(content)
        
        score = score_resume(parsed_info)

        st.write("Extracted Information:")
        for key, value in parsed_info.items():
            st.write(f"{key}: {value}")
        
        st.write(f"Resume Score: {score}/100")

        if st.button("Add Applicant"):
            add_applicant(parsed_info, score, content)
            st.success("Applicant added successfully!")

    display_applicants(get_applicants())
    search_interface(search_applicants)