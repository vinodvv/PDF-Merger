# PDF Merger (CLI + Desktop GUI)

A simple PDF Merger tool built with Python and PyPDF2.

The project contains:
* A **Beginner Command Line script** that merges all PDF files in a folder into a single PDF.
* An **Advanced Desktop GUI app (Tkinter)** that lets users select specific PDF files, choose an output name, and merge them with a click.
---
## Features
### Command Line Interface

File: `pdf_merger.py`
- Scans a directory (`./Files`) for `.pdf` files.
- Lists the found PDF filenames.
- Merges all of them into `./output/merged.pdf`.

### Desktop GUI App (Advanced)
File: `pdf_merger_advanced.py`
- Built with **tkinter** and **PyPDF**
- Lets users select multiple PDF files via a file dialog.
- Displays the selected files in a list with a count.
- Allows setting a custom output filename.
- Saves the merged file into an `output` folder.

---
## Installation
1. Clone the repository:
```bash
  git clone https://github.com/vinodvv/PDF-Merger.git
  cd PDF-Merger
```
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:
```bash
  pip install PyPDF2
```
Tkinter is included with most standard Python installations.

---
## Usage
### Command Line Interface
1. Place your PDF files in the directory `Files` directory.
2. Run:
```bash
  python pdf_merger.py
```
- The script will:
  - Find all `.pdf` files in `./Files`.
  - Print how many files were found and list their names.
  - Create `./Output/merged.pdf` containing all PDFs combined.

### Desktop GUI App
1. Run:
```bash
  python pdf_merger_advanced.py
```
2. In the GUI:
- Click **"Select PDF files** and choose one or more PDFs.
- Optionally change the output filename in the **Output** field.
- Click **"Merge"** to create the merged PDF in the `output` folder.
- A status label and message box will confirm the output filename.

---
## Roadmap / Ideas
- Allow reordering of selected PDFs before merging.
- Add a "Remove selected file" button in the GUI.
- Drag-and-drop support.
- Remember last used folder and output directory.

---
## License
This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.

