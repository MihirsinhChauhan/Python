class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q{self.question_num} : {current_question.text}  (true/false)? ")
        self.check_ans(user_ans,current_question.answer)

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def check_ans(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_num}")
        print("\n")