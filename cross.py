import sys

# Read the Sudoku grid
sudoku = []
for _ in range(9):
    sudoku.append(list(input().strip()))  # Read row as a list of characters

# Function to check if a number can be placed at (row, col)
def is_valid(row, col, num):
    num = str(num)

    # Check row
    if num in sudoku[row]:
        return False

    # Check column
    for x in range(9):
        if sudoku[x][col] == num:
            return False

    # Check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_start_row + i][box_start_col + j] == num:
                return False

    return True  # Number can be placed

# Function to find the only possible position for a number in a 3x3 box
def cross_hatching():
    updated = False  # Track if any changes were made

    for num in range(1, 10):  # Check numbers 1-9
        num = str(num)  # Convert to string for comparison

        # Iterate through each 3x3 box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                # Track possible placements for this number in the box
                possible_positions = []

                for i in range(3):
                    for j in range(3):
                        row, col = box_row + i, box_col + j
                        if sudoku[row][col] == "." and is_valid(row, col, num):
                            possible_positions.append((row, col))

                # If there is exactly **one** possible position, place the number
                if len(possible_positions) == 1:
                    row, col = possible_positions[0]
                    sudoku[row][col] = num
                    updated = True

    return updated

# **Solve Sudoku using cross-hatching**
while True:
    if not cross_hatching():  # If no changes were made, stop
        break

# **Check if there are still empty spaces (which means the puzzle is unsolvable)**
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == ".":
            print("ERROR")  # Unsolvable Sudoku
            sys.exit(0)

# **Print the final solved Sudoku grid**
for row in sudoku:
    print("".join(row))  # Join elements of each row for correct output format
