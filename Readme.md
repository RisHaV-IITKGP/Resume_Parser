## Resume Parser
![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/RisHaV-IITKGP/Resume_Parser)
[![Maintenance](https://img.shields.io/badge/Deployed-yes-green.svg)](https://github.com/RisHaV-IITKGP/Resume_Parser)

This is a python based application which can extract certain useful information about
the applicant from his/her resume.<br>
As of now , the application can extract the following details from the Applicant's resume 

    Name
    Email Address
    Phone Number
    Skills
    Education
    
The application uses the Regular Expressions library to search for patterns like email address ,
phone number. The spacy NLP module is used to tokenize the resume text and search for names 
, skills and education degree.

## Requirements
Following is the list of python libraries required

    re
    nltk
    spacy
    pandas
    pdfminer

Spacy is an Industrial-Strength Natural Language Processing(NLP) tool 
which is used here to detect Indian Names in the resume. <br> After pip installing 
spacy make sure that you install 'xx' model which supports Multi-languages and the English
module.
  
    pip install spacy
    spacy download xx_ent_wiki_sm
    spacy download en_core_web_sm

Using the pdfminer library one can easily extract text from PDF files

    pip install pdfminer.six

## Instructions to use :

* First clone the repository
  
      $ git clone
  
* Now set the directory to the one which contains the extracted files.
* Save your resume with the file name, resume.pdf in the same directory.
* Rum main.py
      
      $ python main.py
  
* All the required information will be produced as output
  in a file 'info.txt' in the same directory.

## Snapshot of Output :

![alt text](https://raw.githubusercontent.com/RisHaV-IITKGP/Resume_Parser/master/Sample_Output.JPG)