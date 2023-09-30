class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, choice):
        return choice == self.correct_choice

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            print(question.text)
            for i, choice in enumerate(question.choices, start=1):
                print(f"{i}. {choice}")

            user_choice = input("Enter the number of your choice: ")
            
            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(question.choices):
                    if question.is_correct(user_choice):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print(f"Wrong! The correct answer was {question.correct_choice}.\n")
                else:
                    print("Invalid choice. Please enter a valid number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        self.show_score()

    def show_score(self):
        total_questions = len(self.questions)
        print(f"You got {self.score} out of {total_questions} questions correct!")

if __name__ == "__main__":
    question1 = Question("What is the capital of France?", ["Paris", "London", "Berlin"], 1)
    question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus"], 1)
    question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2)

    quiz_questions = [question1, question2, question3]

    quiz = Quiz(quiz_questions)
    quiz.run()
