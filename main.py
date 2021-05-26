

# Import the regular expressions library
# Python has a very powerful library called regular expressions
# that handles the task of searching and extracting text quite elegantly.
import re




# spaCy is a free open-source library for Natural Language Processing in Python.
# Command to install library : pip install spacy
# Also we need the Multi-language spaCy module to read names and the English module
# To download this module type in cmd : spacy download xx_ent_wiki_sm/en_core_web_sm
import spacy





# Library Used : pdfminer
# Command to install library : pip install pdfminer.six
# Using the pdfminer library one can easily extract text from PDF files
from pdfminer.high_level import extract_text





# import the pandas library to be used for processing the csv files
import pandas as pd



# import and generate all stopwords to be removed
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))





# An email generally consists of 4 parts :
# Starting text : A sting which may contain lower case alphabets , numbers , '.' , '-' or '_'
# @ symbol in the middle seperating the 1st part form the rest of the parts
# Name of the provider : A sting which may contain lower case alphabets , numbers , '.' , '-' or '_'
# '.' operator followed by 'com' or 'co.in' or 'co.xx'.
EMAIL_PATTERN = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

PHONE_NUMBER_PATTERN = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')


# Common Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 'MASTERS',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'ISC'
        ]



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
    # load pre-trained model

    nlp = spacy.load('xx_ent_wiki_sm')
    doc = nlp(r1)
    for ent in doc.ents:
        if (ent.label_ == 'PER'):
            return ent.text



# Function to extract the skills of the applicant using spacy nlp module
def extract_skills(resume_text):
    # load pre-trained model
    nlp = spacy.load('en_core_web_sm')

    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]

    # reading the csv file
    data = pd.read_csv("skills.csv")

    # extract values
    skills = list(data.columns.values)

    skillset = []

    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    return [i.capitalize() for i in set([i.lower() for i in skillset])]



# Function to extract the Education degree of the applicant
def extract_education(resume_text):
    # load pre-trained model
    nlp = spacy.load('en_core_web_sm')

    nlp_text = nlp(resume_text)


    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education



# driver function
if __name__ == '__main__':

    f = open('info.txt', 'w')

    resume_text = extract_text_from_pdf('./resume.pdf')


    person_names = extract_names(resume_text)
    pos = len(person_names) - 1

    # The first valid name that appears above others is generally the applicant’s actual name,
    # since people tend to place their contact details in the header section of their resumes.
    for i in range(0, len(person_names)):
        if person_names[i] == '\n':
            pos = i
            break

    # Extracting the first name
    name = person_names[:pos + 1]
    f.write('\nName of Applicant : ' + name + '\n\n')




    list_of_emails = extract_emails(resume_text)

    # The first email that appears above others is generally the applicant’s actual email address,
    # since people tend to place their contact details in the header section of their resumes.
    f.write('Applicants Email Address : ')
    if len(list_of_emails) > 0 :
        f.write(list_of_emails[0])
    f.write('\n\n')




    list_of_phone_numbers = extract_phone_numbers(resume_text)

    f.write('Applicants Phone Number : ')
    if len(list_of_phone_numbers) > 0 :
        if len(list_of_phone_numbers[0]) > 9 and len(list_of_phone_numbers[0]) <13 :
            f.write(list_of_phone_numbers[0])
    f.write('\n\n')





    # Extracting skills
    f.write('Applicants Skills : \n\n')
    skills = extract_skills(resume_text)
    for data in skills :
        f.write(data + '\n')
    f.write('\n')




    # Extracting Education
    f.write('Applicants Education : \n\n')
    education = extract_education(resume_text)
    for data in education :
        f.write(data + '\n')
    f.write('\n')

