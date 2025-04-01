# Simple Quiz Game

def ask_question(question, options, correct_answer):
    """Ask the user a question and return if the answer was correct."""
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user's input and convert to an integer (assuming valid input)
    answer = int(input("Enter your choice (1-4): "))

    # Check if the answer is correct (adjust index by -1)
    return options[answer - 1] == correct_answer

def run_quiz():
    """Run the quiz by asking all questions and tracking the score."""
    questions = {
        "What is the capital of France?": 
            (["Paris", "Berlin", "Madrid", "Rome"], "Paris"),
        
        "What is 5 + 7?": 
            (["10", "11", "12", "13"], "12"),

        "Which animal is known as the King of the Jungle?": 
            (["Lion", "Elephant", "Tiger", "Giraffe"], "Lion"),

        "What is the chemical symbol for water?": 
            (["O2", "H2", "H2O", "CO2"], "H2O")
    }

    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    print("-" * 30)

    # Loop through the questions and ask them
    for question, (options, correct_answer) in questions.items():
        if ask_question(question, options, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")

    print("-" * 30)
    print(f"You answered {score} out of {total_questions} questions correctly!")

# Run the quiz
run_quiz()
1