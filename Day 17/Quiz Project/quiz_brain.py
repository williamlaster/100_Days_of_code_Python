class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number} {question.text} (True/False): ").title()
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}.")
            print(
                f"Your score is {self.score}/{self.question_number}.")
            print("\n")
        else:
            print("You got it wrong!")
            print(f"The correct answer was: {correct_answer}.")
            print(
                f"Your score is {self.score}/{self.question_number}.")
            print("\n")
