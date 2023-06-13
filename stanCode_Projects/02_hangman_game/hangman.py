"""
File: hangman.py
Name: Bright Yeh
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. keep the random word
    2. count the turns when there is wrong guess
    3. check the format until correct
    4. for case-insensitive, upper the input alphabet
    5. break the while loop when turns is over
    6. check where's the alphabet one by one and replace it
    7. keep the answer
    8. break the while loop when all correct
    """
    ans = ''
    wrong_ans = ''
    rw = random_word()  # keep the random word
    turns = 0  # count the turns when there is wrong guess
    for i in range(len(rw)):
        ans += '-'
    print('The word looks like ' + ans)  # the tip for the beginning
    while True:
        hangman(turns, wrong_ans)
        print('You have ' + str(N_TURNS - turns) + ' wrong guesses left.')
        input_ch = input('Your guess: ').upper()  # for case-insensitive
        while len(input_ch) != 1 or not input_ch.isalpha():  # for format error, until correct
            print('Illegal format.')
            input_ch = input('Your guess: ')
        n = rw.find(input_ch)
        if n == -1:  # add turns if guess wrong
            if wrong_ans.find(input_ch) == -1:
                turns += 1
                wrong_ans += input_ch  # record wrong answers
                print('There is no ' + input_ch + '\'s in the word. ')
            else:
                print('You guessed \'' + input_ch + '\' wrong before, try again.')  # check the wrong ans
        if turns == 7:  # break the while loop when turns is over
            hangman(turns, wrong_ans)
            print('You are completely hung : (')
            break
        else:
            ans_new = ''  # start from another empty string, thanks TA for this tips !!!
            for i in range(len(rw)):  # check where's the alphabet one by one and replace it
                if input_ch == rw[i]:
                    ans_new += rw[n]
                else:
                    ans_new += ans[i]
            ans = ans_new  # keep the answer
            if ans == rw:  # break the while loop when all correct
                winman(wrong_ans)
                print('You are correct!')
                print('You win!!')
                break
            print('The word looks like ' + ans)
    print('The word was: ' + rw)


def hangman(turns, wrong_ans):
    """
    0                   1                   2                   3
    ______              ______              ______              ______
    |....|              |....|              |....|              |....|
    |....               |...(.)             |...(.)             |...(.)
    |...                |...                |....|              |.../|
    |....               |....               |....|              |....|
    |...                |...                |...                |...
    |..7 left           |..6 left           |..5 left           |..4 left
    -----------         -----------         -----------         -----------
    Wrong ans:          Wrong ans:          Wrong ans:          Wrong ans:

    4                   5                   6                   7
    ______              ______              ______              ______
    |....|              |....|              |....|              |....|
    |...(.)             |...(.)             |...(.)             |...(x)
    |.../|\\            |.../|\\            |.../|\\            |.../|\\
    |....|              |....|              |....|              |....|
    |...                |.../               |.../.\\            |.../.\\
    |..3 left           |..2 left           |..1 left           |.YOU DIED
    -----------         -----------         -----------         -----------
    Wrong ans:          Wrong ans:          Wrong ans:          Wrong ans:
    """
    t = turns
    # column
    print('======')
    print('|    |')
    # head
    print('|   ', end='')
    if t == 0:
        print('')
    elif t == 7:
        print('(x)')
    else:
        print('( )')
    # body
    print('|   ', end='')
    if t == 2:
        print(' |')
    elif t == 3:
        print('/|')
    elif t > 3:
        print('/|\\')
    else:
        print('')
    if t > 1:
        print('|    |')
    else:
        print('|')
    # leg
    print('|   ', end='')
    if t == 5:
        print('/')
    elif t > 5:
        print('/ \\')
    else:
        print('')
    # info
    if t != 7:
        print('|  ' + str(7-t) + ' left')
    else:
        print('| YOU DIED')
    # ground
    print('-----------')
    # show the wrong ans
    if len(wrong_ans) != 0:
        print('Wrong ans: : ' + wrong_ans)
    else:
        print('')


def winman(wrong_ans):
    """
    ======
    |....l
    |
    |...(o)
    |...\\|/
    |....|
    |.../.\
    -----------
    YOU'RE ALIVE!
    """
    print('======')
    print('|    l')
    print('|YOU\'RE ALIVE!')
    print('|   (o)')
    print('|   \\|/')
    print('|    |')
    print('|   / \\')
    print('-----------')
    print('Wrong ans: : ' + wrong_ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
