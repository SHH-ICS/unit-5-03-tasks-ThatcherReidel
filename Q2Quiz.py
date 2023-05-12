# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
# Open the questions file for reading
with open("questions.txt", "r") as f:
    questions = f.readlines()

# Initialize the score
score = 0

# Loop through each question and ask the user
for i, question in enumerate(questions):
    # Split the question and answer using the delimiter
    question, answer = question.split("::")
    # Ask the user the question and get their answer
    user_answer = input(f"Question {i+1}: {question.strip()} ")
    # Check if the user's answer is correct and update the score if necessary
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {answer.strip()}")

# Print the final score
print(f"You got {score} out of {len(questions)} questions correct.")