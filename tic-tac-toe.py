# ---Global variables---

# Game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]


# If game is still going
# When game is over this will change to false
game_still_going = True
# Who won? Or Tie? 
winner = None
# Who's turn is it (X goes first)
current_player = "X"

# ---Functions--- 

# Play a game of tic tac toe 
def play_game():
  while True:
    # Display title of the game
    title_display()
    # Display initial board
    display_board()

    # Infinite loop to alternate turns while game is going game going
    while game_still_going:
      # handle a single turn of an arbitary player
      handle_turn(current_player)  

      #Check if game has ended 
      check_if_game_over()

      # Flip to other player 
      flip_player()
    # The game has ended 
    if winner == "X" or winner == "O":
      print(winner + " won.")
    elif winner == None:
      print("It's a tie.")
    # Offer restart choice or exit program
    choice = input("""Restart (R + Enter)
Exit (Press Any Other Key + Enter)
""")
    if choice == "r" or choice == "R":
      reset_game_settings()
      continue
    else: 
      exit()


# Display the title of the game 
def title_display():
  print(" ")
  print("-------------")
  print("-Tic Tac Toe-")
  print("-------------")
  print(" ")

# Display the game board 
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + "      1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "      4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "      7 | 8 | 9")

# Resets the game conditions of the last previous game played
def reset_game_settings():
  #Declaration of global variables 
  global game_still_going
  global winner
  global current_player
  global board

  game_still_going = True
  winner = None
  current_player = "X"
  board[0] = "-" 
  board[1] = "-"
  board[2] = "-"
  board[3] = "-"
  board[4] = "-"
  board[5] = "-"
  board[6] = "-"
  board[7] = "-"
  board[8] = "-"


# Handles a single turn of an arbitary player
def handle_turn(player):

  # Retrieves position from player 
  print(player + "'s turn.")
  position_index = input("Choose a position from 1 - 9: ")

  # Ensure user enters a valid input
  valid = False;
  while not valid: 
    while position_index not in ["1","2","3","4","5","6","7","8","9"]:
      position_index = input("Choose a position from 1 - 9: ")

    #retrieves the correct index of the board 
    position_index = int(position_index) - 1

    # Check to make sure the spot is available on the board
    if board[position_index] == "-":
      valid = True
    else:
      print("You cant go there. Go again.")
  
  #Put the game piece on the board 
  board[position_index] = player
    
  # Show game board
  display_board()


# Checking the state of the game post-game
def check_if_game_over():
  check_for_winner()
  check_if_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set for global variables 
  global winner 

  # Check for winner based anywhere
  # Check rows
  row_winner = check_rows()
  # Check columns
  column_winner = check_columns()
  # Check diagonals 
  diagonal_winner = check_diagonals()

  # Check if any win condition has been satisfied
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set up global variables 
  global game_still_going
  # Check if any of the rows have all the same values (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win 
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None 


# Check the columns for a win 
def check_columns():
  # Set up global variables 
  global game_still_going
  # check if any of the rows have all the same values (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any column does have a match, flag that there is a win 
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return None 


# Check the diagonals for a win
def check_diagonals():
  # Set up global variables 
  global game_still_going
  # Check if any of the rows have all the same values (and is not empty)
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
  # If any diagonals does have a match, flag that there is a win 
  if diagonals_1 or diagonals_2:
    game_still_going = False
  # Return the winner (X or O)
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[2]
  # Return None if there was no winner
  return None 


# Check if there is a tie
def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  else:
    return False


# Alternates the turns after a player has made a move 
def flip_player():
  # global variables we need 
  global current_player
  # If the current player is X, then switch it to O
  if current_player == "X":
    current_player = "O"
  # If the current player is O, then switch it to X
  elif current_player == "O":
    current_player = "X"


# --- Start Execution ---
# Play game of tic tac toe
play_game()

