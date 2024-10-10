# src/app.py
import os
import tkinter as tk

from ui.interface import DocxToExcelApp

def main():
    root = tk.Tk()
    app = DocxToExcelApp(root)
    
    # Update to use the correct path and icon format (.ico)
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
    root.wm_iconbitmap(icon_path)
    
    root.mainloop()

if __name__ == "__main__":
    main()
