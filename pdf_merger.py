from PyPDF2 import PdfMerger
from pathlib import Path
from datetime import datetime
import re
import sys

BASE_DIR = Path("./Files")
OUTPUT_DIR = Path("./Output")

def natural_sort_key(path):
    """Sort files naturally (e.g., file2.pdf before file10.pdf)"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', str(path.name))]


def main():
    # Validate input directory
    if not BASE_DIR.exists():
        print(f"Error: Directory '{BASE_DIR}' not found")
        exit(1)

    # Find PDF files
    pdf_files = sorted(BASE_DIR.glob("*.pdf"), key=natural_sort_key)

    num_pdfs = len(pdf_files)
    if num_pdfs == 0:
        print("No PDF files found")
        exit(0)

    print(f"\nFound {num_pdfs} PDF files.\n")

    # List filenames
    for filename in pdf_files:
        print(f"+ {filename.name}")

    # Create merger and merge files
    merger = PdfMerger()
    successful = 0
    failed = 0

    print("\nMerging files....")
    for i, pdf in enumerate(pdf_files, start=1):
        try:
            merger.append(str(pdf))
            successful += 1
            print(f"[{i}/{num_pdfs}] ✔️ {pdf.name}")
        except Exception as e:
            failed += 1
            print(f"[{i}/{num_pdfs}] ❌ {pdf.name}: {e}")

    # Check if any files were successfully merged
    if successful == 0:
        print("\nError: No files could be merged")
        merger.close()
        sys.exit(1)

    # Create output directory and generate filename
    OUTPUT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = OUTPUT_DIR / f"merged_{timestamp}.pdf"

    # Save merged PDF
    try:
        with open(output_filename, 'wb') as file:
            merger.write(file)
        merger.close()

        print(f"\n✔️ Successfully merged {successful} file(s)")
        if failed > 0:
            print(f"❌ Failed to merge {failed} file(s)")
        print(f"\nOutput: {output_filename}")

    except Exception as e:
        print(f"\nError saving merged PDF: {e}")
        merger.close()
        sys.exit(1)


if __name__ == "__main__":
    main()
