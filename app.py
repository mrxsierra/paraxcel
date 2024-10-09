# app.py main entry point
import tkinter as tk

from src.ui.interface import DocxToExcelApp

if __name__ == "__main__":
    root = tk.Tk()
    app = DocxToExcelApp(root)
    root.mainloop()