def main():
    choice = int(input("Enter 1 for Single Player, 2 for Multiplayer: ")) # Choice for single player and multiplayer
    board = [0,0,0,0,0,0,0,0,0]  # Initialization of board
    if(choice==1):
        print("Computer: 0 vs You: X")
        player_number = int(input("Enter to 1 to play 1st or 2 to play 2nd: ")) # Choice to play first or second
        for i in range(0,9):
            if(analyze_board(board)!=0):
                break
            # (i+player)%2 to check the turn is of player 1(human) or player 2(computer)
            elif((i+player_number)%2==0): # computers turn
                comp_turn(board)
            else:
                const_board(board)
                user1_turn(board)
    else:
        for i in range(0,9):
            if(analyze_board(board)!=0):
                break
            # (i+player)%2 to check the turn is of player 1 for player 2
            if((i+player_number)%2==0): # player 1 turn
                const_board(board)
                user1_turn(board)
            else:
                const_board(board)
                user2_turn(board)

    result = analyze_board(board)
    if(result==0):
        const_board(board)
        print("Draw")
    if(result==-1):
        const_board(board)
        print("X won")
    if(result==1):
        const_board(board)
        print("O won")

def const_board(board):
    print("Current state of Board: \n")
    for i in range (0,9):
        if((i>0) and (i%3==0)):
            print("\n")
        if(board[i]==0):
            print("_", end=" ")
        if(board[i]==-1):
            print("X ", end=" ")
        if(board[i]==1):
            print("O ", end=" ")
    print("\n\n")

def user1_turn(board):
    pos = int(input("Enter X's position from (1,2,3...9): "))
    # while(board[pos-1]!=0):
    #   print("Wrong Move")
    if(board[pos-1]!=0):
        print("Wrong Move")
        exit(0)
    else:
        board[pos-1] = -1
    
def user2_turn(board):
    pos = int(input("Enter X's position from (1,2,3...9): "))
    # while(board[pos-1]!=0):
    #   print("Wrong Move")
    if(board[pos-1]!=0):
        print("Wrong Move")
        exit(0)
    else:
        board[pos-1] = 1

def analyze_board(board):
    cases = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cases[i][0]]!=0 and 
           board[cases[i][0]]==board[cases[i][1]] and 
           board[cases[i][0]]==board[cases[i][2]]):
            return board[cases[i][0]]
        else:
            return 0

def comp_turn(board):
    pos = -1
    value = -2
    for i in range(0,9):
       if(board[i]==0):
           board[i]=1
           score = -minmax(board,-1) #min max score
           board[i] = 0
           if(score>value):
               value=score
               pos=i
               print(f"Score {score} after {i}")
               print(f"Value  {value} after {i}")
               print(f"[Pos] {pos} after {i}")   
    board[pos]=1

def minmax(board, player):
    win = analyze_board(board)
    if(win!=0):
        return(win*player)
    else:
        pos = -1
        value = -2
        for i in range(0,9):
            if(board[i]==0):
                board[i]=player
                score = -minmax(board,player*-1) #min max score
                board[i] = 0
                if(score>value):
                    value=score
                    pos=i 
        if(pos==-1):
            return 0
        else:
            return value