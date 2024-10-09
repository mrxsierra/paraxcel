from docx.document import Document
from docx import Document as docx_instance
from pydantic import ValidationError
from .para_utility import inject_html_font_formats, remove_prefix, find_marked_answer
from .model import Question

def read_docx(file_path: str) -> Document:
    """Read a DOCX file and return the Document object."""
    return docx_instance(file_path)

def parse_para(doc: Document, breaker: int = 5) -> list[Question]:
    """
    Parse the paragraphs of the DOCX file and extract questions and options.

    Args:
        doc (Document): The docx Document object.
        breaker (int): The number of lines to break for questions and options (default is 5).

    Returns:
        list[Question]: List of parsed Question objects.
    """
    questions: list[Question] = []
    question: list[str] = []
    count: int = 0
    correct_answer: int | None = None

    for para in doc.paragraphs:
        text = para.text.strip()

        if text:
            injected_text = inject_html_font_formats(para)
            text = text if injected_text is None else injected_text
            text = remove_prefix(text)

            # Append the processed text to the question list
            question.append(text)
            count += 1  # Increment count for each option or question

            # Attempt to find the marked answer
            answer = find_marked_answer(para, count)
            correct_answer = correct_answer if answer is None else answer

            # After reading the question and 4 options (5 items in total), save and reset
            if count == breaker:
                # Store the question in the list (correct_answer may be None)
                try:
                    print(answer)
                    questions.append(Question(
                        question_text=question[0],
                        options=question[1:],
                        correct_answer=correct_answer  # This may be None
                    ))
                except ValidationError as e:
                    print(f"Error in validation: {e.json()}")  # Handle invalid data

                # Reset for the next question
                question = []
                count = 0
                correct_answer = None

    # Handle the case where the last question may not have exactly 5 lines but still valid
    if question:
        questions.append(Question(
            question_text=question[0],
            options=question[1:],
            correct_answer=correct_answer
        ))

    return questions

if __name__ == "__main__":
    doc = read_docx("tests/data/doc.docx")
    parsed_questions = parse_para(doc)
    print(parsed_questions)
    print(parsed_questions.__len__())
