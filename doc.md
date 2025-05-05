# 📃 Paraxcel Technical Documentation

This document explains the inner workings, key components, and function/class responsibilities of the Paraxcel DOCX-to-Excel converter application.

## Design Choices

### Data Validation

We use Pydantic for data validation in the `Question` model. This ensures that the data extracted from DOCX files is correctly formatted and valid before being processed further. Pydantic was chosen for its ease of use and powerful validation capabilities, which help maintain data integrity throughout the application.

### GUI with Tkinter

Tkinter was chosen for its simplicity and ease of use. It provides a straightforward way to create a graphical interface for file selection and output management. The decision to use Tkinter was based on its wide availability in standard Python installations and its ability to create a functional GUI with minimal code.

### File Parsing and Export

The parsing logic in `docx_parser.py` is designed to handle various formats of questions and options in DOCX files. The `excel_writer.py` module ensures that the parsed data is correctly formatted and saved into an Excel file, making it easy to analyze and manage. The choice to use `python-docx` for reading DOCX files and `pandas` for handling Excel files was driven by their robustness and extensive documentation.

## 🔧 Core Modules Overview

### `interface.py` (GUI)

#### `DocxToExcelApp`

A class representing the main Tkinter application window.

* `__init__(self, root: tk.Tk)`

  * Initializes the GUI layout.
* `create_widgets(self)`

  * Creates and places all Tkinter widgets.
* `select_file(self)`

  * Opens file dialog to select `.docx` file.
* `select_folder(self)`

  * Opens dialog to select output folder.
* `start_task(self)`

  * Triggers conversion from DOCX to Excel.

### `docx_parser.py` (DOCX Parser)

#### `read_docx(file_path: str) -> Document`

* Uses `python-docx` to load DOCX file.
* Returns a `Document` object.

#### `parse_para(doc: Document, breaker: int = 5) -> list[Question]`

* Extracts questions and their options.
* Assumes every question is followed by 4 options.
* Supports marking of answers by font color/highlight.

### `excel_writer.py` (Excel Export)

#### `para_to_excel(questions: list[Question], save_path: str, columns: list[str])`

* Uses `pandas.DataFrame` and `to_excel` method.
* Saves structured questions/options to Excel.

### `para_utility.py` (Text Handling)

#### `inject_html_font_formats(para: Paragraph) -> str | None`

* Wraps superscript/subscript/italic elements with appropriate HTML-like tags.

#### `remove_prefix(text: str) -> str`

* Strips out leading numbering like "Q1."

#### `find_marked_answer(para: Paragraph, count: int) -> int | None`

* Inspects text color/highlight to detect marked correct option.

### `model.py` (Validation)

#### `Question`

* `question_text: str`: Main question text
* `options: list[str]`: List of 4 option strings
* `correct_answer: Optional[int]`: 0-based index if available

#### `ParsedDoc`

* Container for list of `Question` objects

## 💼 Data Flow Summary

1. User selects DOCX via GUI.
2. `read_docx()` loads the file.
3. `parse_para()` parses paragraphs into `Question` objects.
4. `para_to_excel()` saves the extracted data into `.xlsx` format.

## 📊 Building Executables

Using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=src/assets/icon.ico --name=paraxcel src/app.py \
  --add-data "src/assets/icon.ico;assets" \
  --hidden-import=docx --hidden-import=openpyxl.cell._writer
```

The output will be in `dist/` or as defined.

## 👍 Best Practices

* Use well-formatted DOCX files (see `sample/`).
* Validate DOCX content before conversion.
* Consider enabling logging for debugging or audit trails.

## Conclusion

Paraxcel simplifies the process of converting DOCX files with questions into an Excel format, making it easier to manage and analyze question-based documents. The combination of Pydantic for data validation, Tkinter for the GUI, and robust parsing and export logic ensures a reliable and user-friendly application. This project demonstrates the effective use of Python libraries to create a practical tool for educators and professionals.

## 👋 Contribution

Feel free to fork, suggest changes, or contribute by creating PRs. This project is actively maintained.
