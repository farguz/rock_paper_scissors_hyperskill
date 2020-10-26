# https://hyperskill.org/projects/78/stages/435/implement
import random


def ask_name():
    name = input('Enter your name: ')
    print('Hello, {}'.format(name))
    return name


def ask_options():
    option_list = input()
    if len(option_list) == 0:
        return ['rock', 'paper', 'scissors']
    return option_list.split(',')


def read_rating_file(name):
    rating_file = open('rating.txt', 'r')
    for line in rating_file:
        if name in line:
            name, score = line.split()
            rating_file.close()
            return int(score)
    rating_file.close()
    return 0


def change_score(result, score):
    score = int(score)
    if result == 'win':
        score += 100
        return score
    elif result == 'draw':
        score += 50
        return score


def who_win(comp_choice, player_choice, option_list):
    while comp_choice != option_list[len(option_list) // 2]:
        option_list.append(option_list.pop(0))
    if option_list.index(player_choice) > option_list.index(comp_choice):
        return 'win'
    else:
        return 'loss'


# ask name and find out score (or start with score 0 if no such player), ask options
name = ask_name()
score = read_rating_file(name)
option_list = ask_options()
print('Okay, let\'s start')

while True:
    # easy checks, right input and command to quit
    player_choice = input()

    if player_choice == '!exit':
        print('Bye!')
        break
    elif player_choice == '!rating':
        print(score)
        continue
    elif player_choice not in option_list:
        print('Invalid input')
        continue

    # computer choose rock/paper/scissors/etc
    random.seed()
    comp_choice = random.choice(option_list)

    # check who win and update the score for current player
    if comp_choice == player_choice:
        print('There is a draw ({})'.format(comp_choice))
        score = change_score('draw', score)
        continue
    else:
        result = who_win(comp_choice, player_choice, option_list)
    if result == 'loss':
        print('Sorry, but the computer chose {}'.format(comp_choice))
    if result == 'win':
        print('Well done. The computer chose {} and failed'.format(comp_choice))
        score = change_score('win', score)
