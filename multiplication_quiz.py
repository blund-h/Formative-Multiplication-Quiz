import random

# Creates a dictionary for the difficulty data
difficulty_dict = {1: {"level": "Easy", "max": 5}, 2: {"level": "Medium", "max": 10}, 3: {"level": "Hard", "max": 20}}

# Makes the user select a difficulty level
def difficulty_selection():
    print("\nPlease select a difficulty level before starting the quiz")
    for difficulty_key, difficulty_value in difficulty_dict.items():
        print(f"{difficulty_key}. {difficulty_value['level']} (1–{difficulty_value['max']})")
    
    while True:
        difficulty_selected = input("\nEnter 1, 2 or 3: ")
        if difficulty_selected.isdigit() and int(difficulty_selected) in difficulty_dict:
            return int(difficulty_selected)
        print("Your input was invalid. Please enter 1, 2 or 3 to set the difficulty level: ")

# This creates the random multiplication numbers
def QnA_generator(max_range):
    num1 = random.randint(1, max_range)
    num2 = random.randint(1, max_range)
    correct_answer = num1 * num2
    return num1, num2, correct_answer

# This is what asks the question and checks whether the users answer is correct
def ask_question(question_number, max_range):
    num1, num2, correct_answer = QnA_generator(max_range)
    
    print(f"\nQuestion {question_number}:")
    print(f"What is {num1} x {num2}?")

    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Your input was invalid. Please enter a number next time!")
        return False

    if user_answer == correct_answer:
        print("Yay that's correct! Well done :)")
        return True
    else:
        print(f"Opps that was wrong! The correct answer was {correct_answer}")
        return False

# This starts the quiz
def quiz():
    score = 0

    print("\nHello and welcome to my Times Table Quiz!")

    difficulty = difficulty_selection()
    max_range = difficulty_dict[difficulty]["max"]

    for i in range(1, 5 + 1):
        if ask_question(i, max_range):
            score += 1

    print("\nCongrations! You finished the quiz!")
    print(f"Your score was: {score}/5")

quiz()