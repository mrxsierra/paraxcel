# 💾 Paraxcel: DOCX to Excel Converter

Paraxcel is a lightweight, local-first Python app that allows you to convert Microsoft Word DOCX files containing multiple-choice questions into Excel spreadsheets. Designed for educators, content creators, and assessment professionals, it simplifies data extraction and formatting.

> 🔗 **Video Demo**: [Watch here](https://youtu.be/btjMeafD0vU)

## ✨ Features

* 📄 **DOCX Parsing**: Extracts questions and four answer options per question.
* 📉 **Excel Export**: Saves parsed content into a structured Excel file.
* 🔹 **GUI Interface**: Tkinter-based GUI for intuitive usage.

## 🛠️ Requirements

* Python 3.12 or higher
* Dependencies listed in `requirements.txt`

## 📅 Installation

```bash
# Clone the repository
git clone https://github.com/code50/9698455/tree/main/CS50X/pset/project
cd paraxcel

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Running the App

```bash
python src/app.py
```

Or using [uv](https://pypi.org/project/uv/):

```bash
uv run src/app.py
```

## 📦 Running Executable

If you built the executable using PyInstaller or use the one in `dist-build`:

```bash
cd dist-build
./paraxcel.exe
```

## 🕹️ User Interface Walkthrough

1. **Select File**: Click "Browse" to choose a `.docx` file.
2. **Choose Save Folder**: Select a folder to save the Excel file.
3. **Enter File Name**: Provide a name for the output Excel (without extension).
4. **Click Convert**: Extracts data and saves to `.xlsx`.
5. **Status**: Success or error messages are shown.

## 🌐 Supported Format

* DOCX file should contain:

  * Questions followed by **4 indented options**.
  * Refer to `sample/` folder for ideal formatting examples.

### **✅ Input/Output Snippet (in Markdown)**

```plaintext
Q1. What is the capital of France?
a) Berlin
b) Madrid
c) Paris  <-- (Highlighted or colored)
d) Rome
```

***Becomes in Excel***:

| Question                       | Option 1 | Option 2 | Option 3 | Option 4 | Answer Index |
| ------------------------------ | -------- | -------- | -------- | -------- | ------------ |
| What is the capital of France? | Berlin   | Madrid   | Paris    | Rome     | 2            |

## 📂 Project Structure

```sh
paraxcel/
├── src/
│   ├── app.py                  # Entry point
│   ├── ui/interface.py         # GUI logic
│   └── paraxcel/
│       ├── docx_parser.py      # DOCX reading and parsing
│       ├── excel_writer.py     # Excel writing logic
│       ├── model.py            # Pydantic models
│       └── para_utility.py     # Utility methods
├── tests/                      # Unit tests
├── sample/                     # Sample DOCX files
├── dist-build/                 # Executable builds
└── README.md / doc.md          # Documentation
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## ⚠️ Disclaimer

Paraxcel is under development. Please validate results before use in production.
