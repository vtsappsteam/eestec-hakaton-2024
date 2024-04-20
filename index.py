from transformers import BartTokenizer, BartForConditionalGeneration
import PyPDF2 
from PyPDF2 import PdfReader
# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

reader = PdfReader('Predavanje1.pdf')
extracted_text = ""
for page in reader.pages:
    extracted_text += page.extract_text()

file_name = 'skripta.txt'
import numpy as np
np.savetxt(file_name, [extracted_text], fmt='%s', encoding="utf-8")


file_path = file_name

with open(file_path,encoding="utf-8") as file:
    input_text = file.read()
# Input text to be summarized

# Tokenize and summarize the input text using BART
inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=1000, min_length=500, length_penalty=3.0, num_beams=6, early_stopping=True)

# Decode and output the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Original Text:")
print(input_text)
print("\nSummary:")
print(summary)