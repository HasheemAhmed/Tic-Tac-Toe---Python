# Tic Tac Toe game
def line(size):
    st = str('')

    for x in range((size * 3) + (size - 1)):
        st += '-'

    return st
    
array = list()

def check(size,player):
    for x in range(size):
        sort = True
        for y in array[x]:
            if y == player:
                pass
            else:
                sort = False
                break

        if sort == True: return True

    for x in range(size):
        sort = True
        for y in range(size):
            if array[y][x] == player:
                pass
            else:
                sort = False
                break

        if sort == True: return True

    sort = True
    for x in range(size):
        if array[x][x] == player:
            pass
        else:
            sort = False
            break

    if sort == True: return True

    y = size - 1
    sort = True
    for x in range(size):

        if array[x][y] == player:
            y -= 1
            pass
        else:
            sort = False
            break

    if sort == True: return True

    return False


def board(size):
        for x in range(size):
            for y in array[x]:
                print(f" {y} ",end = '|')
            
            print('\b ')
            if x is not size - 1:
                print(line(size))



def arraySize(size):

    for x in range(size):
        arr2 = list()

        for y in range(size):
            arr2.append(' ')
        
        array.append(arr2)
        del arr2




while(True):
    size = int(input('Enter the Board Size : '))

    arraySize(size)
    game = {'Player 1' : 'O','Player 2':'X'}
    py = ['Player 1','Player 2']
    i = 0
    win = False
    turn = 0
    while(not win):
        print(py[i])
        board(size)
        
        while(True):
            row = int(input('Enter the Row : '))
            col = int(input('Enter the column : '))

            if array[row - 1 ][col - 1 ] == ' ':
                array[row - 1][col -1 ] = game[py[i]]
                turn += 1
                break
            else:
                print("Already Filled.")
                
        
        win = check(size,game[py[i]])
        if win:
            board(size)
            print(py[i], 'wins the match.')
            break
        else:
            if i == 0:
                i = 1
            else:
                i = 0

        if turn == size * size:
            print("Match Drawn.")
            win = True
            break

    if win:
        more = bool(int(input('Do you want to play more ( 1 , 0 )?')))
        if not more:
            break
        del array
        array = list()
        
                  
