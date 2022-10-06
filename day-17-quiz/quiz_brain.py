class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, u_answer, correct_answer):
        if u_answer == correct_answer:
            self.score += 1
            print("Answer is correct!")
        else:
            print("Answer is incorrect! "+correct_answer)

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].text} : ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)



