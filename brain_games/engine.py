import prompt


def engine(game_module, number_of_rounds=3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module()['game_condition'])
    for i in range(number_of_rounds):
        output_of_game_module = game_module()
        print(f"Question: {output_of_game_module['question']}")
        answer = prompt.string('Your answer: ')
        if_right = 'Correct!'
        if_wrong = f"'{answer}' is wrong answer ;(. "\
            f"Correct answer was '{output_of_game_module['right_answer']}'."\
            f"\nLet's try again, {name}!"
        if answer == output_of_game_module['right_answer']:
            print(if_right)
        else:
            return print(if_wrong)
    return print(f"Congratulations, {name}!")
