# src/app.py
import tkinter as tk
from tkinter import PhotoImage
from ui.interface import DocxToExcelApp

def main():
    root = tk.Tk()
    app = DocxToExcelApp(root)
    
    # Alternatively, for .png files, you can use iconphoto()
    root.iconbitmap('src/assets/icon.ico')
    
    root.mainloop()

if __name__ == "__main__":
    main()
