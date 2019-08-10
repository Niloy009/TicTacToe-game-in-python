board = [" " for i in range(9)]

#print function for board

def print_board():
    row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if(icon=='x'):
        number= 1
    elif icon == 'o':
        number = 2
    print("your turn player {}".format(number))
    
    choice = int(input("Please Choose a number (1-9): "))
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print()
        print("Sorry!!The place is fill up..")

def isVictory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon)or\
      (board[3] == icon and board[4] == icon and board[5] == icon)or\
      (board[6] == icon and board[7] == icon and board[8] == icon)or\
      (board[0] == icon and board[3] == icon and board[6] == icon)or\
      (board[1] == icon and board[4] == icon and board[7] == icon)or\
      (board[2] == icon and board[5] == icon and board[8] == icon)or\
      (board[0] == icon and board[4] == icon and board[8] == icon)or\
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
    
                
        
def is_draw():
    if " " not in board:
        return True
    else:
        return False
    
        
while True:
    print_board()
    player_move('x')
    print_board()
    if isVictory('x'):
        print("x wins congratulations")
        break
    elif is_draw():
        print("Its Draw!!")
        break
    player_move('o')
    print_board()
    if isVictory('o'):
        print("o wins congratulations")
        break
    elif is_draw():
        print("Its Draw!!")
        break
    

    
