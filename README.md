# Paraxcel: DOCX to Excel Converter

#### Video Demo: <https://youtu.be/btjMeafD0vU>

#### Description

Paraxcel is a Python tkinter-based application that converts DOCX files with questions and answers into Excel format.

## Overview

Paraxcel is a Python application designed to convert DOCX files containing questions and answers into an Excel format. This tool is particularly useful for educators and professionals who need to manage and analyze question-based documents efficiently. The application provides a user-friendly interface built with Tkinter, allowing users to select DOCX files and save the parsed content into an Excel file.

## Features

- **Read and Parse DOCX Files**: Extract questions and options from DOCX files.
- **Export to Excel**: Save the parsed questions and options into an Excel file.
- **User-Friendly GUI**: Built with Tkinter for easy file selection and output management.

## Limitation
- docx should follow this format:
  - Question + 4 indented options
  - Exmaple doc provided in sample folder

## Requirements

- Python 3.12 or higher
- Required libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   # download
   git clone https://github.com/code50/9698455/tree/main/CS50X/pset/project
   
   # change dir
   cd paraxcel
   # create venv
   python -m venv venv
   # activate venv
   venv\Scripts\activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python src/app.py
   ```

2. Use the GUI to select a DOCX file and specify the output path for the Excel file.

## UV Example
- Install  `pip install uv`
  ```py
  #change dir
  cd paraxcel
  # create venv
  uv run
  # run gui app
  uv run src/app.py
  ```

## Usage Example of Executable

You can also use the executable file located in the `dist-build` folder to run the GUI directly without needing Python. To do so, follow these steps:

1. Navigate to the `dist-build` folder:
    ```bash
    cd dist-build
    ```

2. Run the executable:
    ```bash
    ./paraxcel.exe
    ```

3. The GUI will launch, and you can follow the same steps as described in the User Interface Walkthrough to select and convert DOCX files.

### User Interface Walkthrough

1. **File Selection**:
   - Click the "Browse" button next to the "Select DOCX File" field.
   - A file dialog will open. Navigate to the DOCX file you want to convert and select it.
   - The selected file path will appear in the "Select DOCX File" field.

2. **Folder Selection**:
   - Click the "Browse" button next to the "Select Folder to Save" field.
   - A folder dialog will open. Navigate to the folder where you want to save the Excel file and select it.
   - The selected folder path will appear in the "Select Folder to Save" field.

3. **File Name Entry**:
   - Enter the desired name for the output Excel file in the "Enter File Name" field (without the extension).

4. **Start Conversion**:
   - Click the "Convert" button to start the conversion process.
   - The application will read the selected DOCX file, parse the questions and options, and save them into an Excel file in the specified folder.
   - A success message will appear once the file is saved. If an error occurs, an error message will be displayed.

## Project Structure

- **src/paraxcel/docx_parser.py**: Contains functions to read DOCX files and parse paragraphs into questions and options.
- **src/paraxcel/excel_writer.py**: Provides functionality to convert parsed questions into an Excel file.
- **src/paraxcel/model.py**: Defines the `Question` model using Pydantic for data validation.
- **src/paraxcel/para_utility.py**: Includes utility functions for text processing and finding marked answers in DOCX files.
- **src/ui/interface.py**: Contains the Tkinter-based GUI implementation for the application, allowing users to select files and folders, and start the conversion task.
- **src/app.py**: The main application file that initializes the Tkinter GUI.
- **tests/**: Contains unit tests for various components of the project.
- **sample/**: Sample and ideal document format that give best results for testing.
- **dist-build/**: Contains the executable file to run the GUI, allowing easy access without running the Python script manually.

## Design Choices

### Data Validation

We use Pydantic for data validation in the `Question` model. This ensures that the data extracted from DOCX files is correctly formatted and valid before being processed further. Pydantic was chosen for its ease of use and powerful validation capabilities, which help maintain data integrity throughout the application.

### GUI with Tkinter

Tkinter was chosen for its simplicity and ease of use. It provides a straightforward way to create a graphical interface for file selection and output management. The decision to use Tkinter was based on its wide availability in standard Python installations and its ability to create a functional GUI with minimal code.

### File Parsing and Export

The parsing logic in `docx_parser.py` is designed to handle various formats of questions and options in DOCX files. The `excel_writer.py` module ensures that the parsed data is correctly formatted and saved into an Excel file, making it easy to analyze and manage. The choice to use `python-docx` for reading DOCX files and `pandas` for handling Excel files was driven by their robustness and extensive documentation.

## Building Executable

To build a standalone executable, you can use PyInstaller(windows):
```bash
pyinstaller --onefile --windowed --icon=src/assets/icon.ico --name=paraxcel src/app.py --add-data "src/assets/icon.ico;assets" --hidden-import=docx --hidden-import=openpyxl.cell._writer
```

This command will create a single executable file that includes all necessary dependencies and resources.

## Conclusion

Paraxcel simplifies the process of converting DOCX files with questions into an Excel format, making it easier to manage and analyze question-based documents. The combination of Pydantic for data validation, Tkinter for the GUI, and robust parsing and export logic ensures a reliable and user-friendly application. This project demonstrates the effective use of Python libraries to create a practical tool for educators and professionals.

## Function and Class Documentation

### `src/ui/interface.py`

#### `DocxToExcelApp`

A simple GUI application that allows users to select a DOCX file, select a folder to save the output, enter a file name, and convert the DOCX file to an Excel file.

- `__init__(self, root: tk.Tk)`: Initializes the application with the given Tkinter root.
- `create_widgets(self)`: Creates the widgets for the GUI.
- `select_file(self)`: Opens a file dialog to select a DOCX file.
- `select_folder(self)`: Opens a folder dialog to select a folder to save the output.
- `start_task(self)`: Starts the task of converting the selected DOCX file to an Excel file.

### `src/paraxcel/para_utility.py`

#### `inject_html_font_formats(para: Paragraph) -> str | None`

Inject HTML tags for subscript, superscript, and math expressions in the text.

- **Args**:
  - `para (Paragraph)`: The paragraph to check for formatted text.
- **Returns**:
  - `str or None`: The formatted text, or None if no formatting was found.

#### `remove_prefix(text: str) -> str`

Remove numbering prefixes like 'Q1.' from the text.

- **Args**:
  - `text (str)`: The text to clean.
- **Returns**:
  - `str`: The text without any numbering prefixes.

#### `find_marked_answer(para: Paragraph, count: int) -> int | None`

Find the marked answer based on color or highlighting.

- **Args**:
  - `para (Paragraph)`: The paragraph to inspect for the answer.
  - `count (int)`: The option number (used as the index).
- **Returns**:
  - `int or None`: The index of the correct answer, or None if no marking is found.

### `src/paraxcel/model.py`

#### `Question`

Represents a multiple-choice question.

- **Attributes**:
  - `question_text (str)`: The text of the question. Required.
  - `options (list[str])`: A list of answer options. Required. Must contain at least one option.
  - `correct_answer (Optional[int])`: The index of the correct answer within the `options` list. The index is 0-based. If the correct answer is not known or does not exist, this can be set to `None`. If provided, must be a valid index within the `options` list.

#### `ParsedDoc`

Represents a parsed document containing a list of questions.

- **Attributes**:
  - `questions (list[Question])`: A list of `Question` objects. Required. Must contain at least one question.

### `src/paraxcel/excel_writer.py`

#### `para_to_excel(questions: list[Question], save_path: str, columns: list[str])`

Convert the parsed questions into an Excel file.

- **Args**:
  - `questions (list[Question])`: List of Question objects.
  - `save_path (str)`: The file path to save the Excel file.
  - `columns (list[str])`: The column names for the Excel file.

### `src/paraxcel/docx_parser.py`

#### `read_docx(file_path: str) -> Document`

Read a DOCX file and return the Document object.

- **Args**:
  - `file_path (str)`: The path to the DOCX file.
- **Returns**:
  - `Document`: The docx Document object.

#### `parse_para(doc: Document, breaker: int = 5) -> list[Question]`

Parse the paragraphs of the DOCX file and extract questions and options.

- **Args**:
  - `doc (Document)`: The docx Document object.
  - `breaker (int)`: The number of lines to break for questions and options (default is 5).
- **Returns**:
  - `list[Question]`: List of parsed Question objects.



## Disclaimer

This project is still under development and may contain bugs or inaccuracies.  Use at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.