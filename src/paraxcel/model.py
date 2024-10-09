from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class Question(BaseModel):
    question_text: str = Field(..., description="The text of the question")
    options: list[str] = Field(..., description="A list of answer options")
    correct_answer: Optional[int] = Field(None, ge=1, le=4, description="Index of the correct answer (0-3), can be None if not found")

    class Config:
        json_schema_extra = {
            "example": {
                "question_text": "Which of the following is a supporting activity in a typical value chain?",
                "options": ["Finance", "Distribution", "Service", "Marketing"],
                "correct_answer": 2  # Can also be None
            }
        }

class ParsedDoc(BaseModel):
    questions: list[Question]

    class Config:
        json_schema_extra = {
            "example": {
                "questions": [
                    {
                        "question_text": "Which of the following is a supporting activity in a typical value chain?",
                        "options": ["Finance", "Distribution", "Service", "Marketing"],
                        "correct_answer": 2
                    },
                    {
                        "question_text": "Which of the following is not a typical flow in a supply chain?",
                        "options": ["Material", "Information", "Funds", "Labour"],
                        "correct_answer": 3
                    }
                ]
            }
        }

if __name__ == "__main__":
    # Example of a valid question with a correct answer
    try:
        q_with_answer = Question(
            question_text="What is the capital of France?",
            options=["Berlin", "Madrid", "Paris", "Rome"],
            correct_answer=2  # Valid integer
        )
        print(q_with_answer)

    except ValidationError as e:
        print(f"Validation error: {e.json()}")

    # Example of a question without a correct answer
    try:
        q_without_answer = Question(
            question_text="What is the capital of Spain?",
            options=["Berlin", "Madrid", "Paris", "Rome"],
            correct_answer=None  # No answer found
        )
        print(q_without_answer)

    except ValidationError as e:
        print(f"Validation error: {e.json()}")
