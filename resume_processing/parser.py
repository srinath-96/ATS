from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import re

# Load pre-trained model and tokenizer
model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create NER pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def extract_entities(text, label):
    entities = ner_pipeline(text)
    return " ".join([entity['word'] for entity in entities if entity['entity_group'] == label])

def parse_resume(content):
    # Extract name (assuming it's a person)
    name = extract_entities(content, "PER")

    # Extract email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, content)
    email = email_match.group() if email_match else ""

    # Extract phone number
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phone_match = re.search(phone_pattern, content)
    phone = phone_match.group() if phone_match else ""

    # Extract education (simple approach, can be improved)
    education_keywords = ["degree", "bachelor", "master", "phd", "diploma"]
    education_sentences = [sent for sent in content.split('.') if any(keyword in sent.lower() for keyword in education_keywords)]
    education = ". ".join(education_sentences)

    # Extract work experience (simple approach, can be improved)
    work_keywords = ["experience", "work", "job", "position"]
    work_sentences = [sent for sent in content.split('.') if any(keyword in sent.lower() for keyword in work_keywords)]
    work_experience = ". ".join(work_sentences)

    # Extract skills (simple approach, can be improved)
    skill_pattern = r'skills:(.+?)(?:\n|$)'
    skill_match = re.search(skill_pattern, content, re.IGNORECASE | re.DOTALL)
    skills = skill_match.group(1).strip() if skill_match else ""

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "education": education,
        "work_experience": work_experience,
        "skills": skills
    }