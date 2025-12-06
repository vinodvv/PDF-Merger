"""
Simple Tkinter-based PDF Merger GUI using PyPDF2.

Users can select multiple PDF files, choose an output filename,
and merge them into a single PDF.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

selected_files = []


def select_pdfs():
    """Open a file dialog and store the selected PDF file Paths"""
    global selected_files
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    # Convert to list so it's easier to manipulate
    selected_files = list(files)
    update_list_files()


def update_list_files():
    """Refresh the listbox and file count label with current selections."""
    list_files.delete(0, tk.END)

    for i, file in enumerate(selected_files, start=1):
        # Show only the filename with an index prefix
        file_name = f"{i} - {os.path.basename(file)}"
        list_files.insert(tk.END, file_name)

    # Update file count label
    file_count_label.config(
        text=f"{len(selected_files)} files selected"
    )


def merge_pdfs():
    """Merge the selected PDF files into the specified output file."""
    # Ensure at least one PDF file is selected
    if not selected_files:
        messagebox.showwarning(
            "No files selected",
            "Please select at least one PDF file to merge."
        )
        return

    output_name = output_entry_text.get().strip()

    # Check output filename
    if not output_name:
        messagebox.showwarning(
            "Invalid output filename",
            "Please provide a valid output filename."
        )
        return

    # Ensure the output has a .pdf extension
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    # Ensure output folder exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Full file path where the file will be saved
    full_output_path = os.path.join(output_dir, output_name)

    # Output filename
    output_filename = os.path.basename(full_output_path)

    merger = PdfMerger()

    # Append all selected PDFs
    for pdf in selected_files:
        merger.append(pdf)

    # Write the merged PDF to disk
    with open(full_output_path, 'wb') as file:
        merger.write(file)

    # Update and show status label and message box
    status_label.config(text=f"Merged into: {output_filename}", fg="green")
    messagebox.showinfo("Success", f"Merged into: {output_filename}")


# ----- GUI -----
root = tk.Tk()
root.title('PDF Merger')
root.geometry('480x480')

# Label Title
label_title = tk.Label(root, text="PDF Merger", font=("Arial", 16))
label_title.pack(pady=20)

# Select files button widget
btn_choose_dir = tk.Button(
    text="Select PDF files", font=("Arial", 12), command=select_pdfs
)
btn_choose_dir.pack(pady=10)

# Listbox to display selected files
list_files = tk.Listbox(root, width=60, height=8, font=("Arial", 10))
list_files.pack(pady=10)

# Label showing count of selected files
file_count_label = tk.Label(
    root, text="0 files selected.", font=('Arial', 10)
)
file_count_label.pack()

# Frame to hold the Output label and Entry
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create the Label
output_label = tk.Label(frame, text="Output:", font=("Arial", 12))
output_label.pack(side=tk.LEFT, padx=5, pady=5)

# Output file name
output_entry_text = tk.StringVar(value="merged_output.pdf")

output_entry = tk.Entry(
    frame,
    textvariable=output_entry_text,
    font=("Arial", 12)
)
output_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Merge button
merge_btn = tk.Button(
    root,
    text="Merge",
    font=("Arial", 12),
    command=merge_pdfs
)
merge_btn.pack(pady=10)

# Show status
status_label = tk.Label(root, text="", font=('Arial', 12))
status_label.pack()


# Main loop
root.mainloop()
