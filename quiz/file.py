
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What color are apples?\n(a) Red/Green (b) Orange (c) Blue (d) Yellow",
    "How many days do we have in a week?\n(a) Seven (b) Two (c) Five (d) Four",
    "In which direction does the sunrise?\n(a) East (b) West (c) South (d) North",
    "2+2 = ?\n(a) 9 (b) 4 (c) 5 (d) 2",
    "How many bones does an adult human have?\n(a) 402 b) 108 (c) 206 (d) 99"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    f = open("Relatorio.txt", "w+")
    f.write("you got " + str(score) + " out of " +
            str(len(questions)) + " - " + str((score*100)/len(questions))+"%")
    f.close()


run_quiz(questions)
