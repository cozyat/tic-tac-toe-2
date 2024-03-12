matrix = [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_grid():
    print("  A   B   C")
    row_number = 1
    for row in matrix:
        print(row_number, ' | '.join(row))
        row_number += 1
    print("")

print_grid()

user_choice = input("X or O? ").upper()

location = input("Where? ")

col_map = {'A': 0, 'B': 1, 'C': 2}
row_map = {'1': 0, '2': 1, '3': 2}

if len(location) == 2 and location[0].upper() in col_map and location[1] in row_map:
    col_index = col_map[location[0].upper()]
    row_index = row_map[location[1]]
    
    if matrix[row_index][col_index] == ' ':
        matrix[row_index][col_index] = user_choice
        print_grid()
    else:
        print("That position is already taken.")
else:
    print("Invalid input. Please provide a valid location (e.g., A1, C3, B2).")

def check_win():
    for row in matrix:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(matrix[0])):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != ' ':
            return True

    if (matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ') \
    or (matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != ' '):
        return True

    return False

def check_tie():
    for row in matrix:
        if ' ' in row:
            return False
    return True

while True:
    if check_win():
        print("Congratulations! Player", user_choice, "wins!")
        break
    elif check_tie():
        print("It's a tie!")
        break

    user_choice = 'O' if user_choice == 'X' else 'X'

    location = input("Player " + user_choice + ", where would you like to place your mark? ")

    if len(location) == 2 and location[0].upper() in col_map and location[1] in row_map:
        col_index = col_map[location[0].upper()]
        row_index = row_map[location[1]]

        if matrix[row_index][col_index] == ' ':
            matrix[row_index][col_index] = user_choice
            print_grid()
        else:
            print("That position is already taken.")
    else:
        print("Invalid input. Please provide a valid location (e.g., A1, C3, B2).")
