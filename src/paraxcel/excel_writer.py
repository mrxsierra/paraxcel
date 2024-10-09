import pandas as pd
from .model import Question

def para_to_excel(questions: list[Question], save_path: str, columns: list[str]):
    """
    Convert the parsed questions into an Excel file.

    Args:
        questions (list[Question]): List of Question objects.
        save_path (str): The file path to save the Excel file.
        columns (list[str]): The column names for the Excel file.
    """
    data = [
        [q.question_text] + q.options + [q.correct_answer if q.correct_answer is not None else "No Answer"]
        for q in questions
    ]
    
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(save_path, index=False)

if __name__ == "__main__":
    # Example of writing the parsed questions to Excel
    example_questions = [
        Question(question_text="What is the capital of France?", options=["Berlin", "Madrid", "Paris", "Rome"], correct_answer=2),
        Question(question_text="Which of these is a programming language?", options=["Python", "Snake", "Lizard", "Anaconda"], correct_answer=None)
    ]
    para_to_excel(example_questions, "output.xlsx", ['Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer'])
