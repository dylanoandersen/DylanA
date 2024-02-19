#Author: Dylan Andersen
#10/22/2021
#Connect4

import random

#________________FUNCITONS______________

def display(B):
    rows = len(B)
    cols = len(B[0])
    
    print("  1   2   3   4   5   6   7  ")
    for i in range(0,rows,1):
        print("-----------------------------")
        for j in range(0,cols,1):
            print("|", B[i][j], end=" ")
        print("|")
    print("-----------------------------")
    
    

def check(B):
    #diagnol
    for x in range(5,2,-1):
        for i in range (0,4,1):
            if(B[x][i] == B[x-1][i+1] and B[x][i] == B[x-2][i+2] and B[x][i] == B[x-3][i+3] and B[x][i] != " "):
                return 100
    
    for y in range(5,2,-1):
        for j in range (6,2,-1):
            if(B[y][j] == B[y-1][j-1] and B[y][j] == B[y-2][j-2] and B[y][j]== B[y-3][j-3] and B[y][j] != " "):
                return 100
    #horizontal & vertical
    for z in range(0,6,1):
        for w in range(0,4,1):
            if(B[z][w] == B[z][w+1] and B[z][w] == B[z][w+2] and B[z][w] == B[z][w+3] and B[z][w] != " "):
                return 100
            
    for v in range(0,7,1):
        for e in range(0,3,1):
            if(B[e][v] == B[e+1][v] and B[e][v] == B[e+2][v] and B[e][v] == B[e+3][v] and B[e][v] != " "):
                return 100
            
#modify so it checks that tem_array[r][c] is in B[x][i]
def check3(B, t, d):
    #diagnol
    for x in range(5,1,-1):
        for i in range (0,5,1):
            if(B[x][i] == B[x-1][i+1] and B[x][i] == B[x-2][i+2] and B[x][i] != " "):
                if(B[t][d] == B[x][i] or B[t][d] == B[x-1][i+1] or B[t][d] == B[x-2][i+2]):
                    return 70
    
    for y in range(5,1,-1):
        for j in range (6,1,-1):
            if(B[y][j] == B[y-1][j-1] and B[y][j] == B[y-2][j-2] and B[y][j] != " "):
                if(B[t][d] == B[y][j] or B[t][d] == B[y-1][j-1] or B[t][d] == B[y-2][j-2]):
                    return 70
    
    #horizontal & vertical
    for z in range(0,6,1):
        for w in range(0,5,1):
            if(B[z][w] == B[z][w+1] and B[z][w] == B[z][w+2] and B[z][w] != " "):
                if(B[t][d] == B[z][w] or B[t][d] == B[z][w+1] or B[t][d] == B[z][w+2]):
                    return 70
            
    for v in range(0,7,1):
        for e in range(0,4,1):
            if(B[e][v] == B[e+1][v] and B[e][v] == B[e+2][v] and B[e][v] != " "):
                if(B[t][d] == B[e][v] or B[t][d] == B[e+1][v] or B[t][d] == B[e+2][v]):
                    return 70





def ava(B):
    #available coloums
    col_nums = []
    for i in range (0,7,1):
        if(B[0][i] == " "):
            col_nums.append(i)
    return col_nums


def score(B, C):
    #for the AI 
    temp_array = B.copy()
    
    for i in range(0,len(C),1):
        r = gravity(temp_array,C[i])
        temp_array[r][C[i]] = "O"
        scor = check(temp_array)
        if(scor == 100):
            temp_array[r][C[i]] = " "
            return C[i]
        temp_array[r][C[i]] = " "
    
    for i in range(0,len(C),1):
        r = gravity(temp_array,C[i])
        temp_array[r][C[i]] = "X"
        scor = check(temp_array)
        if(scor == 100):
            temp_array[r][C[i]] = " "
            return C[i]
        temp_array[r][C[i]] = " "
        
    for i in range(0,len(C),1):
        r = gravity(temp_array,C[i])
        temp_array[r][C[i]] = "X"
        scor = check3(temp_array, r, C[i])
        if(scor == 70):
            temp_array[r][C[i]] = " "
            return C[i]
        temp_array[r][C[i]] = " "
    return random.choice(C)
    
    

def validLocation(B, c):
    #if you can place a piece
    if(B[0][c] == "X" or B[0][c] == "O"):
        return True
    

def gravity(B, c):
    #dropping piece to lowest point
    g = 5
    for i in range(0,6,1):
        if(B[i][c] == "X" or B[i][c] == "O"):
            y = i-1
            return y
    return g









#___________________MAIN_____________________

def main():
    gameBoard = [None] * 6
    for i in range(0, len(gameBoard), 1):
        gameBoard[i] = [" "] * 7

    numMoves = 0
    valid = False
    
    #randomize who goes first 
    turn = random.randint(0,1)
    

    while(True):
        if(turn == 0):
            
            #player input
            valid = False
            display(gameBoard)
            #ask for coloum
            c = int(input("Enter col# 1-7: ")) - 1
            valid = validLocation(gameBoard, c)
            
            #check if piece can be placed
            while(valid == True):
                c = int(input("Re-Enter col# 1-7: ")) - 1
                valid = validLocation(gameBoard, c)
            
            #get row number
            r = gravity(gameBoard, c)
            gameBoard[r][c] = "O"
            numMoves = numMoves + 1
            status = check(gameBoard)
            
            turn = turn + 1
            turn = turn % 2
            
            if(status == 100):
                print("You Win")
                break
            
       
        if(turn == 1):
            #computer input
            display(gameBoard)
            
            #get coloum number
            array = ava(gameBoard)
            cc = score(gameBoard, array)
            
            #get row number
            rr = gravity(gameBoard, cc)
            gameBoard[rr][cc] = "X"
            
            numMoves = numMoves + 1
            status = check(gameBoard)
            
            display(gameBoard)
            
            turn = turn + 1
            turn = turn % 2
    
            
            if(status == 100):
                print("Computer Wins")
                break
            
        
        
        
        
        
        
        #undo option
        if(numMoves >= 2):
            undo = int(input("Would you like to undo?\nEnter 1/Yes or 2/No: "))
            
            if(undo == 1):
                gameBoard[r][c] = " "
                gameBoard[rr][cc] = " "
                 
    
        if(numMoves == 50):
            print("Its's a tie")
            break
            

    display(gameBoard)


main()


