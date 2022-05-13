def create_boards(binary_input, board, boards):
  row_index = 0
  board_index = 0 
  # What would be a better design for creating bingo boards from the input? 
  for string in binary_input: 
    clean_line = string.split()
    # Updates board metrics when new line is detected 
    if (len(clean_line) == 0):
      if (board_index > 0): 
        board = []
      row_index = 0 
      board_index += 1
    # Adds lines that contain numbers into the board 
    else: 
      board.append(clean_line) 
    # Adds board to boards array after the final row is added 
    if row_index == 5:
      boards.append(board)
    row_index += 1 
  return board_index

def markBoard(bingo_number, board):
  row_index = 0
  number_index = 0 

  # Goes through board.  When number on board is called, turn the number into a "T" 
  for row in board:
    for number in row:
      if (number == bingo_number):
        board[row_index][number_index] = "T" 
      number_index += 1 
    number_index = 0 
    row_index += 1 
  return

def checkForBingo(board): 
  ts_in_row = 0
  ts_in_column = 0

  # Goes through each number on the board, counting the number of Ts within each row and column
  for i in range(len(board)):
    for j in range(len(board)):
      if (board[j][i] == "T"):
        ts_in_column += 1
      if (board[i][j] == "T"):
        ts_in_row += 1
      # Check to see if a board has 5 Ts in a row  
      if (ts_in_column == 5):
        return True
      if (ts_in_row == 5):
        return True
    ts_in_row = 0
    ts_in_column = 0
  return False 

def findWinningBoard(boards, bingo_numbers):
  numbers_called = 0
  winner = "None" 

  for bingo_number in bingo_numbers: 
    board_index = 0 
    for board in boards: 
      markBoard(bingo_number, board)
      if numbers_called > 4: 
        if (checkForBingo(board) == True):
          return (board_index, bingo_number)
      board_index += 1
    if (winner != "None"):
      break 
    numbers_called += 1

def calculateBoard(board, number_just_called):
  sum = 0
  number_just_called = int(number_just_called) 
  board = list(board[0])
  for row in board:
    for char in row: 
      if (char != "T"):
        char = int(char) 
        sum += char 
  return number_just_called * sum

if __name__ == "__main__":
  board = [] 
  boards = []
  board_index = 0

  # Read each text file line into a string within an array
  with open("day4/input.txt") as values:
    binary_input = values.readlines()
  # Gets rid of bingo numbers from binary input, and separates each number 
  bingo_numbers = binary_input[0]
  binary_input.remove(bingo_numbers)
  bingo_numbers = bingo_numbers.split(',')

  amount_of_boards = create_boards(binary_input, board, boards)
  
  # Removes winning board from boards array until only one remains 
  while (amount_of_boards > 0): 
    board_index, number_just_called = findWinningBoard(boards, bingo_numbers)
    if (amount_of_boards == 1):
      break 
    boards.remove(boards[board_index])
    amount_of_boards -= 1

  answer = calculateBoard(boards, number_just_called)
  print(answer) 