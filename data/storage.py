import pandas as pd
from datetime import datetime

applicants_df = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Education', 'Work Experience', 'Skills', 'Score', 'Resume Text', 'Applied Date'])

def add_applicant(parsed_info, score, resume_text):
    global applicants_df
    new_applicant = pd.DataFrame({
        'Name': [parsed_info['name']],
        'Email': [parsed_info['email']],
        'Phone': [parsed_info['phone']],
        'Education': [parsed_info['education']],
        'Work Experience': [parsed_info['work_experience']],
        'Skills': [parsed_info['skills']],
        'Score': [score],
        'Resume Text': [resume_text],
        'Applied Date': [datetime.now()]
    })
    applicants_df = pd.concat([applicants_df, new_applicant], ignore_index=True)

def get_applicants():
    return applicants_df

def search_applicants(search_term):
    return applicants_df[applicants_df.apply(lambda row: search_term.lower() in str(row).lower(), axis=1)]