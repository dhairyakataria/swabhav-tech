
def create_board(): 
    borad = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return(borad)


def print_board(board):
    print('\n\t', board[0],'  |  ', board[1],'  |  ', board[2])
    print('\t','-'*18)
    print('\t', board[3],'  |  ', board[4],'  |  ', board[5])
    print('\t','-'*18)
    print('\t', board[6],'  |  ', board[7],'  |  ', board[8])

def check_winner(board, player):
    if (board[0] == board[1] == board[2]):         #checking first row
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[3] == board[4] == board[5]:         #checking second row
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[6] == board[7] == board[8]:         #checking third row
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[0] == board[3] == board[6]:         #checking first column
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[1] == board[4] == board[7]:         #checking second column
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[2] == board[5] == board[8]:         #checking third column
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[0] == board[4] == board[8]:         #checking diagonals
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True
    elif board[2] == board[4] == board[6]:         #checking diagonals
        print('\n\tGame Over.  Player ', player ,'Wins!!\n\n')
        return True


def new_game():
    board = create_board()
    print(' Use X for player 1\n Use O for player 2\n')

    count = 0
    player = 1
    while True:
        print_board(board)
        print("Player ", player,".\nMove to which place?")
        move_to = int(input())
        move_to -= 1

        if board[move_to] == 'X' or board[move_to] == 'O':
            print("That place is already filled.")
            continue
        else:
            if player==1:
                board[move_to] = 'X'
            else:
                board[move_to] = 'O'
            count += 1

        if count>4:
            if check_winner(board, player) == True:
                return
        
        if player == 1:
            player = 2
        else:
            player = 1
        
        if count==9:
            print("\tGame Over.\n\tIt's a Tie!!\n\n")
            return
    

if __name__ == '__main__':
    play_again = 'y'
    while play_again == 'y':
        new_game()
        play_again = input('Do want to play Again?(y/n)')