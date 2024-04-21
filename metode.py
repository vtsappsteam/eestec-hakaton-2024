from PyPDF2 import PdfReader
import numpy as np
import pypandoc 

def readPdf(file):
  reader = PdfReader(file)
  extracted_text = ""
  for page in reader.pages:
      extracted_text += page.extract_text()
  file = file.replace("pdf", "txt")
  np.savetxt(file, [extracted_text], fmt='%s', encoding="utf-8")

def readWord(file):
  outFile = file.replace("docx", "txt")
  output = pypandoc.convert_file(file, 'plain', outputfile=outFile)
  assert output == ""
  
  
  
  
