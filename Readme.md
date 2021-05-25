## Resume Parser
![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/RisHaV-IITKGP/Resume_Parser)
[![Maintenance](https://img.shields.io/badge/Deployed-yes-green.svg)](https://github.com/RisHaV-IITKGP/Resume_Parser)

This is a python based application which can extract the name and Email address of
the applicant from his/her resume.<br>
The application uses the Regular Expressions library to extract the Email address
of the applicant and the spacy NLP module to extract the name.

## Requirements
Following is the list of python libraries required

    re
    spacy
    pdfminer

Spacy is an Industrial-Strength Natural Language Processing(NLP) tool 
which is used here to detect Indian Names in the resume. <br> After pip installing 
spacy make sure that you install 'xx' model which supports Multi-languages.
  
    pip install spacy
    spacy download xx_ent_wiki_sm

Using the pdfminer library one can easily extract text from PDF files

    pip install pdfminer.six

## Instructions :

* First clone the repository
  
      $ git clone
  
* Now set the directory to the one which contains the extracted files.
* Save your resume with the file name, Sample_Resume.pdf in the same directory.
* Rum main.py
      
      $ python main.py
  
* The Applicants Email Address and Name will be displayed as Output.

