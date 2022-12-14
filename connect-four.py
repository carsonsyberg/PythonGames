# Connect 4
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _
# _ _ _ _ _ _ _

columns = [['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_'], 
           ['_','_','_','_','_','_']]
           
rows = [['_','_','_','_','_','_','_'], 
        ['_','_','_','_','_','_','_'], 
        ['_','_','_','_','_','_','_'], 
        ['_','_','_','_','_','_','_'], 
        ['_','_','_','_','_','_','_'], 
        ['_','_','_','_','_','_','_']]
           
column_fill_level = [0, 0, 0, 0, 0, 0, 0]

def print_board():
    for r in rows:
        for col in r:
            print(col + ' ', end =" ")
        print('')

def checkRows():
    # loop through each row
    for r in rows:
        # loop through each col 
        prevChar = '_'
        charMatchCounter = 0
        for col in r:
            if(col == prevChar and col != '_'):
                charMatchCounter += 1
                if(charMatchCounter >= 3):
                    return True
            else:
                charMatchCounter = 0
            prevChar = col
            
    return False

def checkCols():
    # loop through each col
    for c in columns:
        # loop through each row 
        prevChar = '_'
        charMatchCounter = 0
        for row in c:
            if(row == prevChar and row != '_'):
                charMatchCounter += 1
                if(charMatchCounter >= 3):
                    return True
            else:
                charMatchCounter = 0
            prevChar = row
            
    return False

def checkDiagonals():
    # loop through rows 0, 1, 2, 3
    rowNum = 0
    for r in rows[0:3]:
        # loop through cols 0, 1, 2, 3
        colNum = 0
        for c in r[0:4]:
            # check if 4 \ diagonals equivalent
            diagEqual = True
            for i in range(1, 4):
                if(c != rows[rowNum + i][colNum + i]):
                    diagEqual = False
            if(diagEqual and c != '_'):
                return True
            colNum += 1
        # loop through cols 6, 5, 4, 3
        colNum = 6
        for c in reversed(r[3:7]):
            # check if 4 \ diagonals equivalent
            print(rowNum, colNum)
            diagEqual = True
            for i in range(1, 4):
                if(c != rows[rowNum + i][colNum - i]):
                    diagEqual = False
            if(diagEqual and c != '_'):
                return True
            colNum -= 1
        rowNum += 1
        
    return False

def checkConnectFour():
    # need to check rows for 4 adjacent equal chars
    if(checkRows()):
        return True
    # need to check cols for 4 adjacent equal chars
    if(checkCols()):
        return True
    # need to check one of them for 4 diagonally adjacent equal chars
    if(checkDiagonals()):
        return True
        
    return False

def play_game():
    connectFour = False
    
    # need a var to track whose turn it is
    currTurn = True
    
    token_char = '_'
    
    # need a game loop that ends when someone gets 4 in a row
    print_board()
    while not connectFour:
        if currTurn:
            token_char = 'X'
        else:
            token_char = 'O'
        # need to get input: select a column to drop token
        valid_input = False
        while not valid_input:
            col_string = input('Which column do you drop your ' + 
                                token_char + ' token in? [0-6]\n')
            col = -1
            if col_string.isnumeric():
                col = int(col_string)
                if col < 0 or col > 6:
                    print('That value is outside the range,' 
                          + ' please enter a column number from [0-6].')
                elif column_fill_level[col] > 5:
                    print('That column is full, please choose another.\n')
                else:
                    valid_input = True;
                    print('Valid input given...')
            else:
                print('The value must be a column number from [0-6].')
            # need to validate input
                # cannot have col be one of the full columns
                # cannot have col be less than 0 or greater than 6
        # END WHILE
        # add token to columns and rows arrays
            # col == input column
            # row == 0 + column_fill_level[col]
        columns[col][column_fill_level[col]] = token_char
        rows[5-column_fill_level[col]][col] = token_char
        # add to column_fill_level[col]
        column_fill_level[col] = column_fill_level[col] + 1
        # check for 4 in a row
        connectFour = checkConnectFour()
        # check for a full board
            # if board full -> set connectFour to draw
        # then change whose turn it is and print board
        currTurn = not currTurn
        print_board()
    # END WHILE
    print('Player with ' + token_char + ' token has won!')
    
play_game()
