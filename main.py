import os

#**Global Variable used :
board = [" 1 "," 2 "," 3 ",
        " 4 "," 5 "," 6 ",
        " 7 "," 8 "," 9 "]


#**Methods used :

#This method displays the board in real-time scenario
def dispBoard():
  print("   "+"|"+"   "+"|"+"   ")
  print(board[0]+"|"+board[1]+"|"+board[2])  
  print("   "+"|"+"   "+"|"+"   ")
  
  print("   "+"|"+"   "+"|"+"   ")
  print(board[3]+"|"+board[4]+"|"+board[5])  
  print("   "+"|"+"   "+"|"+"   ")
  
  print("   "+"|"+"   "+"|"+"   ")
  print(board[6]+"|"+board[7]+"|"+board[8])  
  print("   "+"|"+"   "+"|"+"   ")
  
#Method called before every move to take user input and make necessary changes to the board position
def handleTurn(move):
  print("move # "+str(move))  #To decide whose turn it is
  if move%2==0:
    print("player O to move.")
  else:
    print("player X to move.")

  position = input("Choose a position between 1-9: ")

  while position not in ["1","2","3","4","5","6","7","8","9"]:  #To neglect any input other than 1-9
    position = input("Choose a position between 1-9: ")

  position = int(position)-1

  #Check whether a position is already occupied otherwise assign X/O to the position
  if board[position]==" O ": 
    return 0
  elif board[position]==" X ":
    return 2
  else:
    if move%2==0:
      board[position]=" O "
    else:
      board[position]=" X "
    return 1


# Clear output screen function
def clear():
    os.system( 'clear' )


#main function that calls all other auxilliary functions
def playGame():
  move=1

  while 1:                    #indefinite loop with break used wherever necessary
    dispBoard()
    print("\n\n")
    
    m=handleTurn(move)
    
    if(move>4):               # Time saving condition! Game can only stop after atleast 4 moves. 
      r=checkGameOn(move)     # Check if game will still go to next move/if someone won/game tied.
      
      if r==0:
        if m==1:
          move=move+1
      elif r==2:
        print("Match has tied!")
        break
      else:
        if move%2==0:
          clear()
          print("\nPlayer O won the Game !!\n\n")
          dispBoard()
        else:
          clear()
          print("\nPlayer X won the Game !!\n\n")
          dispBoard()
        break
    
    else:
      if(m==1):
        move=move+1
    clear()
    
    if m==2:
      print("Player X has already played that move!")
    elif m==0:
      print("Player O has already played that move!")  


def checkGameOn(move):    #Checks if someone has won/game has tied, otherwise continue the game
  if(checkWin()):
    return 1
  elif checkTie(move):
    return 2
  else:
    return 0


def checkCols():          #Check for a X/O sequence in all three columns
  for i in range(3):
    if board[3*i]==board[3*i+1]==board[3*i+2]:
      return 1
  return 0


def checkRows():          #Check for a X/O sequence in all three rows
  for i in range(3):
    if board[i]==board[i+3]==board[i+6]:
      return 1
  return 0


def checkDiag():          #Check for a X/O sequence in both diagonals
  if board[0]==board[4]==board[8]:
    return 1
  if board[6]==board[4]==board[2]:
    return 1
  return 0


def checkWin():           #Declares a win if any row/column/diagnol has three X/O
  if(checkCols()):
    return 1
  if(checkRows()):
    return 1    
  if(checkDiag()):
    return 1

  return 0


def checkTie(move):       #Declares the game tied if all moves have been played and noone has won yet.
  if move>=9:
    if checkWin()==0:
      return 1
  
  return 0


#Driver Function calls the main function to play the game.
playGame()
