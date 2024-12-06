def read_input_to_2d_array(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        array_2d = [list(line.strip()) for line in lines]
    return array_2d

filename = 'day6/input6.txt'
array_2d = read_input_to_2d_array(filename)
for row in array_2d:
    print(row)

up_arrow = "^"
down_arrow = "v"
left_arrow = ">"
right_arrow = "<"
empty_space = "."
wall = "#"

def find_start(array_2d):
    arrow_chars = {up_arrow, down_arrow, left_arrow, right_arrow}
    row_id = 0
    col_id = 0
    for row in array_2d:
        for char in row:
            if char in arrow_chars:
                return char, col_id, row_id
            col_id += 1
        col_id = 0
        row_id += 1

def get_coordinate_above(col, row, array_2d):
    if row - 1 < 0:
        return False
    return col, row - 1

def get_coordinate_below(col, row, array_2d):
    if row + 1 >= len(array_2d):
        return False
    return col, row + 1

def get_coordinate_left(col, row, array_2d):
    if col - 1 < 0:
        return False
    return col - 1, row

def get_coordinate_right(col, row, array_2d):
    if col + 1 >= len(array_2d[0]):
        return False
    return col + 1, row

def get_char_at_coordinate(col, row, array_2d):
    if 0 <= row < len(array_2d) and 0 <= col < len(array_2d[0]):
        return array_2d[row][col]
    return False

def try_move_up(col, row, array_2d):
    if get_char_at_coordinate(col, row - 1, array_2d) == empty_space:
        return col, row - 1
    elif get_char_at_coordinate(col, row - 1, array_2d) == wall:
        return col + 1, row
    else:
        return -1, -1

def try_move_down(col, row, array_2d):
    if get_char_at_coordinate(col, row + 1, array_2d) == empty_space:
        return col, row + 1
    elif get_char_at_coordinate(col, row + 1, array_2d) == wall:
        return col - 1, row
    else:
        return -1, -1

def try_move_left(col, row, array_2d):
    if get_char_at_coordinate(col - 1, row, array_2d) == empty_space:
        return col - 1, row
    elif get_char_at_coordinate(col - 1, row, array_2d) == wall:
        return col, row - 1
    else:
        return -1, -1

def try_move_right(col, row, array_2d):
    if get_char_at_coordinate(col + 1, row, array_2d) == empty_space:
        return col + 1, row
    elif get_char_at_coordinate(col + 1, row, array_2d) == wall:
        return col, row + 1
    else:
        return -1, -1

char, start_col, start_row = find_start(array_2d)

inside_lab = True
num_spaces = 0
col = start_col
row = start_row
current_char = get_char_at_coordinate(col, row, array_2d)

while inside_lab:
    num_spaces += 1
    if current_char == up_arrow:
        col, row = try_move_up(col, row, array_2d)
    elif current_char == down_arrow:
        col, row = try_move_down(col, row, array_2d)
    elif current_char == left_arrow:
        col, row = try_move_left(col, row, array_2d)
    elif current_char == right_arrow:
        col, row = try_move_right(col, row, array_2d)
    if col == -1:
        inside_lab = False