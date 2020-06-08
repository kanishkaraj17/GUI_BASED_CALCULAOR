from IPython.display import clear_output

lists = [' '] * 10
lists[0] = '#'


def board():
    clear_output()
    print(lists[1] + '|' + lists[2] + '|' + lists[3])
    print('-----')
    print(lists[4] + '|' + lists[5] + '|' + lists[6])
    print('-----')
    print(lists[7] + '|' + lists[8] + '|' + lists[9])


def win(mark):
    return ((lists[1] == lists[2] == lists[3] == mark) or (lists[4] == lists[5] == lists[6] == mark) or (
                lists[7] == lists[8] == lists[9] == mark) or (lists[1] == lists[5] == lists[9] == mark) or (
                        lists[3] == lists[5] == lists[7] == mark))


def blank(position):
    return lists[position] == ' '


def game():
    choose = input("choose 'X' or 'O'").upper()
    if (choose == 'X'):
        First_player = choose
    else:
        second_player = choose
    turn = 'first'
    while (1):
        if (' ' not in lists):
            print('Draw')
            break
        elif (turn == 'first'):
            print('player 1 turn')
            position = int(input('Enter your position'))
            if (blank(position)):
                lists[position] = 'X'
                board()
            else:
                print('Give correct position')
            if (win('X')):
                print("player 1 wins")
                break
            else:
                turn = 'second'
        elif (turn == 'second'):
            print('player 2 turn')
            position = int(input('Enter your position'))
            if (blank(position)):
                lists[position] = 'O'
                board()
            else:
                print('Give correct position')
            if (win('O')):
                print("player 2 wins")
                break
            else:
                turn = 'first'


if __name__ == '__main__':
    while (1):
        game()
        lists = [' '] * 10
        replay = input("Replay 'Y' or 'N'").upper()
        if (replay == 'Y'):
            continue
        else:
            print('Thank you')
            break
