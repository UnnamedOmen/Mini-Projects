# list of questions
# store the answers

# randomly pick questions
# ask the questions
# see if they are correct
# keep track of score
# tell the user their score

import random

questions = {
    "What keyword is used to define a function in Python?": "def",
    "What data type does the input() function return?": "str",
    "What symbol is used to start a comment?": "#",
    "What method adds an item to the end of a list?": "append()",
    "What keyword is used to handle exceptions?": "try",
    "What built-in function returns the number of items in a list?": "len()",
    "What operator is used for floor division?": "//",
    "What keyword creates a loop that repeats while a condition is true?": "while",
    "What data type is created using curly braces { } with key-value pairs?": "dict",
    "What statement is used to stop a loop early?": "break",
    "What function converts a string into an integer?": "int()",
    "What keyword is used to import a module?": "import",
    "What is the value of bool(0)?": "False",
    "What method removes and returns the last item from a list?": "pop()",
    "What is the output of print(type([]))?": "<class 'list'>"
}

def python_python_trivia_game(questions):
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Enter your answer: ").lower().strip()
        correct_answer = questions[question].lower()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorecct, the correct answer is: {correct_answer}")
    print(f"Final score is: {score}/{total_questions}")

    

python_python_trivia_game(questions)