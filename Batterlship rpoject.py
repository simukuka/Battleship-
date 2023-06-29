ships_grid = [
    ["B", "B", "B", "E"],
    ["E", "E", "E", "E"],
    ["E", "B", "E", "B"],
    ["E", "B", "E", "B"],
]

guesses_grid = [
    ["E", "E", "E", "E"],
    ["E", "E", "E", "E"],
    ["E", "E", "E", "E"],
    ["E", "E", "E", "E"],
]


def print_grid(my_list):
    """
    Prints a 2D grid.

    Args:
        my_list (list): A 2D list representing the grid.
    """
    for row in my_list:
        print(row)


num_hits = 0
num_misses = 0
while num_hits < 7 or num_misses < 9:
    print_grid(guesses_grid)
    user_row = int(input("Enter the row for your guess (0-3): "))
    user_col = int(input("Enter the column for your guess (0-3): "))

    # Validate user input
    if (user_row > 3 or user_row < 0) or (user_col > 3 or user_col < 0):
        print("Please choose a valid row and column")
        continue
    elif guesses_grid[user_row][user_col] != "E":
        print("Enter a row and column you have not already guessed")
        continue
    elif ships_grid[user_row][user_col] == "B":
        # Handle a hit
        guesses_grid[user_row][user_col] = "H"
        print("You Hit!")
        num_hits += 1
    elif ships_grid[user_row][user_col] == "E":
        # Handle a miss
        guesses_grid[user_row][user_col] = "M"
        print("You missed!")
        num_misses += 1

# Game over, check if the player won or lost
if num_hits == 7:
    print("Congratulations, you sunk all my battleships!")
    print_grid(guesses_grid)
else:
    print("Sorry, you lose...")
    print_grid(guesses_grid)
