"""
Would you like to play "Noughts and Crosses"?
Two players, take turns, up to 5*5 grid.
Move is a two-digit number. 00 is upper-left corner, nn - lower right corner,
where n is the size of your grid.
"""

import random


def get_dimension():
    dim = 0
    while not dim:
        dim_input = input("Choose the dimension for the grid < 6 ('q' to end the game): ")
        if dim_input == 'q':
            return 0
        try:
            dim = int(dim_input)
        except ValueError:
            print("Usage: a number from 2 to 5.")
            continue
        if dim > 5:
            print("Please, choose a number < 6.")
            dim = 0
    return dim


def is_any_vacant(grid, dim):
    for i in range(dim):
        try:
            grid.index("_")
        except ValueError:
            return False
    return True


def is_grid_full(grid, dim):
    result = True
    for i in range(dim):
        if is_any_vacant(grid[i], dim):
            result = False
    return result


def print_grid(grid, dim):
    line = ""
    for i in range(dim):
        for j in range(dim):
            line += grid[i][j] + " "
        print(line)
        line = ""


def get_position(dim):
    while True:
        msg = "Enter grid position for your move: (q for exit)"
        position = input(msg)
        error_msg = "Please, enter two numbers les: row column."
        if position == 'q':
            return 0
        elif len(position) != 2:
            print(error_msg)
            continue
        try:
            row = int(position[0])
            column = int(position[1])
            if row > dim - 1 or column > dim - 1:
                raise ValueError
        except ValueError:
            print(error_msg)
            continue
        break
    return row, column


def get_vacant_pos(grid, dim):
    result = []
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == "_":
                result.append((i, j))
    return result


def change_in_position(grid, position, symbol):
    result = 0
    row = position[0]
    column = position[1]
    if grid[row][column] is "_":
        grid[row][column] = symbol
        result = 1
    else:
        print("You can't write into that position.")
        result = 0
    return result


def check_line(grid, position, dim, steps):
    px, py = position
    dx, dy = steps
    p = grid[px][py]
    if p == "_":
        return False
    while True:
        px += dx
        py += dy
        if px >= dim or py >= dim or px < 0 or py < 0:
            break
        if grid[px][py] is not p:
            return False
    return True


def is_win(grid, dim):
    result = False
    for d1, d2 in zip([0, 1, 1], [1, 0, 1]):
        line = check_line(grid, (0, 0), dim, (d1, d2))
        if line:
            return True
    line = check_line(grid, (dim - 1, 0), dim, (-1, 0))
    if line:
        return True
    return result


def play_game(grid, dim):
    win = False
    symbol = ""
    move_count = 1
    while not is_grid_full(grid, dim):
        if move_count % 2 == 0:
            symbol = "0"
            p = get_position(dim)
        else:
            symbol = "x"
            p = get_position(dim)
        if not p:
            print("The game is over")
            return True

        if not change_in_position(grid, p, symbol):
            continue
        else:
            move_count += 1
            print_grid(grid, dim)

        if is_win(grid, dim):
            print("You win!!!")
            win = True
            return True

    if not win:
        print("It's a draw.")
        return True


def main():
    cancel_msg = "The game is over"
    dim = get_dimension()
    if dim:
        grid = [["_" for i in range(dim)] for j in range(dim)]
    else:
        print(cancel_msg)
        return

    print_grid(grid, dim)
    play_game(grid, dim)


if __name__ == '__main__':
    main()