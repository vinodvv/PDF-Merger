from PyPDF2 import PdfMerger
import os

BASE_DIR = "./Files"

merger = PdfMerger()

pdf_files = []
for file in os.listdir(BASE_DIR):
    if file.lower().endswith(".pdf"):
        pdf_files.append(os.path.join(BASE_DIR, file))

# Number of PDFs
num_pdfs = len(pdf_files)

print(f"\nFound {num_pdfs} PDF files.\n")

# List filenames
for filename in pdf_files:
    print(f"+ {os.path.basename(filename)}")

# Merge PDF files
for pdf in pdf_files:
    merger.append(pdf)

os.makedirs("Output", exist_ok=True)
output_filename = "Output/merged.pdf"

# Save merged PDF
with open(output_filename, 'wb') as file:
    merger.write(file)

print(f"\nMerged into: {output_filename}.")
