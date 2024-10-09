import re
from docx.text.paragraph import Paragraph

def inject_html_font_formats(para: Paragraph) -> str | None:
    """
    Inject HTML tags for subscript, superscript, and math expressions in the text.

    Args:
        para (Paragraph): The paragraph to check for formatted text.

    Returns:
        str or None: The formatted text, or None if no formatting was found.
    """
    paragraph = ""
    if para.runs:
        for run in para.runs:
            words = run.text.strip()

            # Check for subscript, superscript, or math formatting
            if run.font.math:
                words = f"<math>{words}</math>"
            if run.font.subscript:
                words = f"<sub>{words}</sub>"
            if run.font.superscript:
                words = f"<sup>{words}</sup>"

            paragraph += words  # Append the formatted words

        return paragraph.strip() if paragraph else None
    return None

def remove_prefix(text: str) -> str:
    """
    Remove numbering prefixes like 'Q1.' from the text.

    Args:
        text (str): The text to clean.

    Returns:
        str: The text without any numbering prefixes.
    """
    pattern = r"^[Qq]\d+\.|\d+\."
    match = re.match(pattern, text)
    return text[match.end():].strip() if match else text

def find_marked_answer(para: Paragraph, count: int) -> int | None:
    """
    Find the marked answer based on color or highlighting.

    Args:
        para (Paragraph): The paragraph to inspect for the answer.
        count (int): The option number (used as the index).

    Returns:
        int or None: The index of the correct answer, or None if no marking is found.
    """
    answer: int | None = None
    if para.runs:
        for run in para.runs:
            # Check if this paragraph is the answer (based on color)
            if run and run.font.color and run.font.color.rgb:
                answer = count - 1  # Mark the current option as the answer
                return answer

            # Check if this paragraph is the answer (based on color)
            if run and run.font.highlight_color:
                answer = count - 1 # Mark the current option as the answer
                return answer

