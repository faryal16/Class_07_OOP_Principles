from termcolor import colored

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self, question_number):
        print(colored(f"\nQ{question_number}: {self.question}", 'blue'))
        for option in self.options:
            print(option)

class QuizManager:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.score = 0
        self.total_questions = 0

    def start_quiz(self, topic):
        questions = self.quiz_data.get(topic, [])
        if not questions:
            print("\nNO question found for this topic.")
            return

        self.total_questions = len(questions)
        self.score = 0

        question_number = 1
        for question in questions:
            q = Question(question['question'], question['options'], question['answer'])
            q.display(question_number)
            user_answer = input("\nYour Answer: ")
            if user_answer.lower() == question['answer'][0].lower():
                self.score += 1
                print(colored("\nCorrect ✅", 'green'))
            else:
                print(colored(f"\nWrong ❌ The correct answer was: ", 'red'))
                print(colored(f"\n{question['answer']}", 'green'))

            question_number += 1

        self.display_score()

    def display_score(self):
        print(colored(f"\nQuiz Over! Your Score: {self.score}/{self.total_questions}", 'yellow'))

class UserProgress:
    def __init__(self):
        self.score = {}

    def update_score(self, topic, score, total_questions):
        self.score[topic] = {'score': score, 'total': total_questions}

    def view_score(self):
        print(colored("\nYour Progress:", 'magenta'))
        
        if not self.score:
            print(colored("\nYou haven't attempted any quiz yet. 💤", 'yellow'))
            return

        for topic, score_info in self.score.items():
            print(f"{topic}: {score_info['score']}/{score_info['total']}")