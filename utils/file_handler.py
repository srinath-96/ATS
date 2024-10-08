import io
from docx import Document
from PyPDF2 import PdfReader

def read_file_content(uploaded_file):
    if uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join(page.extract_text() for page in pdf_reader.pages)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    else:
        return uploaded_file.getvalue()