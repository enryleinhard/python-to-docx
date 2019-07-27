import docx


file_word = docx.Document()
pilihan = ''
print("Writing in Python to Word")
print("Do you want to continue? (y/n)")
pilihan = input()
if pilihan == 'y':
    print("Let's get started!")
    user = 'y'
    while user != 'n':
        print("Enter Text: ")
        text = input()
        file_word.add_paragraph(text)
        print("Do you want to add another paragraph? (y/n)")
        user = input()
    print("Thanks for using!")
    file_word.save("python-to-word.docx")
    
