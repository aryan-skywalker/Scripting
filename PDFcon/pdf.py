import PyPDF2

with open('Tutor Mentor Interaction.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)
    
    #print(reader.getPage(1))
    
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
