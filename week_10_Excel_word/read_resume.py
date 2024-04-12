import docx  # must do a little more for importing docx - BarTab -> settings -> select project -> Project interpreter

# -> search for docx

document = docx.Document('IT_Sample_Resume.docx')  # uppercase D in .Document, as always file must be typed exactly as
# it is saved, including .docx

for para in document.paragraphs:  # this will pull paragraphs in document indicated
    if 'ethical hacking' in para.text.lower():
        print('An ethical hacker!!')  # this will check the document to find text indicated, and give us the output
        # message assigned if so, and we don't need to open the doc, unless we want to double-check ourselves
#    print(para.text) # output will be text from document

