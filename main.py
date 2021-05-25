

# Import the regular expressions library
# Python has a very powerful library called regular expressions
# that handles the task of searching and extracting text quite elegantly.
import re




# spaCy is a free open-source library for Natural Language Processing in Python.
# Command to install library : pip install spacy
# Also we need the Multi-language spaCy module to read names
# To download this module type in cmd : spacy download xx_ent_wiki_sm
import spacy




# Library Used : pdfminer
# Command to install library : pip install pdfminer.six
# Using the pdfminer library one can easily extract text from PDF files
from pdfminer.high_level import extract_text




# An email generally consists of 4 parts :
# Starting text : A sting which may contain lower case alphabets , numbers , '.' , '-' or '_'
# @ symbol in the middle seperating the 1st part form the rest of the parts
# Name of the provider : A sting which may contain lower case alphabets , numbers , '.' , '-' or '_'
# '.' operator followed by 'com' or 'co.in' or 'co.xx'.
EMAIL_PATTERN = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

PHONE_NUMBER_PATTERN = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')



# Function to extract text from the resume
def extract_text_from_pdf(path) :
    return extract_text(path)



# Function to extract the list of all emails present in the resume
def extract_emails(resume_text):
    return re.findall(EMAIL_PATTERN, resume_text)


# Function to extract the list of all phone numbers present in the resume
def extract_phone_numbers(resume_text):
    return re.findall(PHONE_NUMBER_PATTERN, resume_text)



# Function to extract the name of the applicant using spaCy's Multi-Language module
def extract_names(resume_text):
    person_names = []

    r1 = str(resume_text)
    nlp = spacy.load('xx_ent_wiki_sm')
    doc = nlp(r1)
    for ent in doc.ents:
        if (ent.label_ == 'PER'):
            return ent.text



# driver function
if __name__ == '__main__':

    resume_text = extract_text_from_pdf('./Sample_Resume.pdf')

    list_of_emails = extract_emails(resume_text)

    # The first email that appears above others is generally the applicant’s actual email address,
    # since people tend to place their contact details in the header section of their resumes.
    if len(list_of_emails) > 0 :
        print('Applicants Email Address : ' + list_of_emails[0])




    list_of_phone_numbers = extract_phone_numbers(resume_text)

    if len(list_of_phone_numbers) > 0 :
        print('Applicants Phone Number : ' + list_of_phone_numbers[0])




    person_names = extract_names(resume_text)
    pos = len(person_names) - 1

    # The first valid name that appears above others is generally the applicant’s actual name,
    # since people tend to place their contact details in the header section of their resumes.
    for i in range(0,len(person_names)) :
        if person_names[i] == '\n' :
            pos = i
            break

    # Extracting the first name
    name = person_names[:pos+1]
    print('Applicants Name : ' + name)


