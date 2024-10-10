# src.ui.interface.py

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from paraxcel.docx_parser import read_docx, parse_para
from paraxcel.excel_writer import para_to_excel

class DocxToExcelApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("paraxcel: Get Question Paper in Excel")
        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        # File selection
        self.file_label = tk.Label(self.root, text="Select File:")
        self.file_label.pack(pady=5)
        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack(pady=5)
        self.file_button = tk.Button(self.root, text="Browse", command=self.select_file)
        self.file_button.pack(pady=5)

        # Folder selection
        self.folder_label = tk.Label(self.root, text="Select Folder to Save:")
        self.folder_label.pack(pady=5)
        self.folder_entry = tk.Entry(self.root, width=50)
        self.folder_entry.pack(pady=5)
        self.folder_button = tk.Button(self.root, text="Browse", command=self.select_folder)
        self.folder_button.pack(pady=5)

        # File name input
        self.file_name_label = tk.Label(self.root, text="Enter New File Name:")
        self.file_name_label.pack(pady=5)
        self.file_name_entry = tk.Entry(self.root, width=50)
        self.file_name_entry.pack(pady=5)

        # Start task button
        self.start_button = tk.Button(self.root, text="Start Task", command=self.start_task)
        self.start_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Docx files", "*.docx")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select a folder to save the file")
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)

    def start_task(self):
        selected_file = self.file_entry.get()
        folder = self.folder_entry.get()
        file_name = self.file_name_entry.get()

        if not selected_file:
            messagebox.showerror("Error", "Please select a file!")
            return
        if not folder:
            messagebox.showerror("Error", "Please select a folder to save!")
            return
        if not file_name:
            messagebox.showerror("Error", "Please enter a file name!")
            return

        save_file_path = os.path.join(folder, file_name + ".xlsx")

        try:
            content = read_docx(selected_file)
            questions = parse_para(content)
            para_to_excel(questions, save_file_path, columns=['Question', 'Option A', 'Option B', 'Option C', 'Option D', 'correct_answer'])
            messagebox.showinfo("Success", f"File saved as {save_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
