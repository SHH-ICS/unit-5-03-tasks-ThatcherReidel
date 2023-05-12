# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
question = input("Enter the question: ")
optionA = input("Enter option A: ")
optionB = input("Enter option B: ")
optionC = input("Enter option C: ")
optionD = input("Enter option D: ")
correctAnswer = input("Enter the correct answer (A/B/C/D): ")

with open("questions.txt", "a") as file:
    file.write(question + "\n")
    file.write("A. " + optionA + "\n")
    file.write("B. " + optionB + "\n")
    file.write("C. " + optionC + "\n")
    file.write("D. " + optionD + "\n")
    file.write("Answer: " + correctAnswer + "\n\n")