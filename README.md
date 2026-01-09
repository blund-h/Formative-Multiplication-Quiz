# Formative-Multiplication-Quiz
## Description
A simple python quiz app which runs in the terminal that allows you to test your times tables skills with randomly generated questions. The test allows you to pick from three difficulties
## User Documentation
The multiplication quiz is a 5 question randomly generated quiz to help you develop your multiplication skills. To support your learning, if you incorrectly answer a question, the correct answer will be displayed before moving on to the next question.
### 1.	Start / Run the Quiz
Once the program is started you will see a welcome message introducing the quiz
### 2.	Choose a difficulty
You will be asked to select one of the following:

<img width="602" height="101" alt="Picture1" src="https://github.com/user-attachments/assets/e95f1de7-a809-4f27-b0a9-eb39caaabae8" />

The numbers in brackets eg (1-5) shows the smallest and largest times tables you may be tested on.

Please type 1, 2 or 3 to match the corresponding difficulty and click enter. You will not be able to continue the quiz without entering one of these values.
### 3.	Answer the Questions
The quiz includes 5 multiplication questions for you to answer.
For each question:
•	Type only your answer
•	Press Enter
•	Then you will be told if your answer is correct or incorrect
If your answer is incorrect the correct answer will be displayed before the next question.
Please ensure to type only numbers for your answers. Any other input will prompt a warning message, and the question will be skipped earning you no point towards your final score.

<img width="602" height="104" alt="Picture2" src="https://github.com/user-attachments/assets/a115fb20-3c93-4eee-bd38-40fb47d45604" />

### 4.	View your Score
Once you have answered all 5 questions the quiz is finished and your final score will be displayed.

## Technical Documentation
### How to run the Program
#### Clone the Repo
To start working with the app you can clone the GitHub repository which involves taking a local copy for your computer to view, edit and run the project.

To download the GitHub repository, you can use command-line instructions in the terminal using the code below.

```bash
git clone https://github.com/ blund-h/Formative-Multiplication-Quiz.git
```
You then can paste the below code into the terminal to move inside of the folder you have just cloned
```bash
cd Formative-Multiplication-Quiz
```
Alternatively you can use Visual Studio Code to manually select the cloned app through ‘File/Open Folder’

Since the quiz does not require any additional libraries there is no extra installation necessary.

## Program Structure
The program is in a single python file which needs no extra installations unless you do not have Python installed on your computer.

### Difficulty System
The quiz uses a dictionary to store the various difficulty levels

```python
difficulty_dict = {1: {"level": "Easy", "max": 5},2: {"level": "Medium", "max": 10},3: {"level": "Hard", "max": 20}}
```
The max value controls how big the multiplications numbers can be generated in the questions.

### Functions
`difficulty_selection()`
- Displays difficulty options
-	Asks for user input
-	Checks the input is valid
-	Returns the chosen difficulty level
  
`QnA_generator(max_range)`
-	Creates two random numbers within the selected difficulties range
-	Calculates the correct answer
-	Returns the two numbers and the answer to be used in ask_question
  
`ask_question(question_number, max_range)`
-	Asks a question using the two numbers generated from QnA_generator(max_range)
-	Asks for user input
-	Checks if it is invalid, if so, it returns a warning prompt and skips the question
-	Checks if it is correct or incorrect
-	Returns True or False
  
`quiz()`
-	Runs the full quiz
-	Keeps the score of correct answers
-	Asks 5 randomly generated questions
-	Displays the final score to the user and ends the quiz
