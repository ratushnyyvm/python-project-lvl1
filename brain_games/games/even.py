import random


def even():
    output = dict.fromkeys(['game_condition', 'question', 'right_answer'])
    output['game_condition'] = 'Answer "yes" if the number is even, '\
        'otherwise answer "no".'

    question = random.randrange(100)
    output['question'] = question

    right_answer = "yes" if question % 2 == 0 else "no"
    output['right_answer'] = right_answer

    return output
