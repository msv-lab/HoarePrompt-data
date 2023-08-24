def draw_brackets(n, sequence):
    # create the initial empty grid with the required width and height
    width = n * 2 - 1
    height = n * 2 - 1
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # fill in the grid based on the sequence of brackets
    for i in range(n):
        if sequence[i] == '[':
            # calculate the start and end positions of the brackets
            start_row = i * 2 - 1
            end_row = (n - i - 1) * 2 + 1
            start_col = i * 2
            end_col = (i + 1) * 2 - 1

            # draw the vertical lines of the brackets
            for j in range(start_row, end_row):
                grid[j][start_col] = '|'
                grid[j][end_col] = '|'

            # draw the horizontal lines of the brackets
            for j in range(start_col + 1, end_col):
                grid[start_row][j] = '-'
                grid[end_row][j] = '-'

    # create the final string representation of the brackets
    bracket_string = ''
    for row in grid:
        bracket_string += ''.join(row) + '\n'

    return bracket_string.rstrip()

# read the input values
n = int(input())
sequence = input()

# draw and print the brackets
result = draw_brackets(n, sequence)
print(result)