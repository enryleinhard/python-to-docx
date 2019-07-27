import docx

doc = docx.Document()
doc.add_paragraph('Hello world!')
doc.add_paragraph('Hello world! x2')
doc.save('demo3.docx')