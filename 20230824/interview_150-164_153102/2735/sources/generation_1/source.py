def rotate_left(arr):
    return [arr[-1]] + arr[:-1]

def rotate_right(arr):
    return arr[1:] + [arr[0]]

def transform_sequence(start, target):
    start_sequence = list(start)
    target_sequence = list(target)
    clicks = 0

    for i in range(8):
        if start_sequence == target_sequence:
            return clicks

        clicked_icon = start_sequence[i]
        click_position = i
        clicks += 1

        if clicked_icon == 'A':
            if click_position != 0:
                start_sequence = rotate_left(start_sequence[:click_position+1]) + \
                                rotate_right(start_sequence[click_position+1:])
            if click_position != 7:
                start_sequence = rotate_right(start_sequence[:click_position]) + \
                                rotate_left(start_sequence[click_position:])
        elif clicked_icon == 'B':
            if click_position != 0 and click_position != 7:
                start_sequence[click_position+1] = start_sequence[click_position-1]
        elif clicked_icon == 'C':
            start_sequence[7-click_position] = chr(ord('A') + (ord(start_sequence[7-click_position]) - ord('A') + 1) % 6)
        elif clicked_icon == 'D':
            if click_position != 0 and click_position != 7:
                start_sequence = rotate_left(start_sequence[:click_position]) + \
                                rotate_right(start_sequence[click_position:])
        elif clicked_icon == 'E':
            if click_position != 0 and click_position != 7:
                y = min(click_position, 7 - click_position)
                start_sequence[click_position-y], start_sequence[click_position+y] = \
                    start_sequence[click_position+y], start_sequence[click_position-y]
        elif clicked_icon == 'F':
            if click_position % 2 == 0:
                start_sequence[click_position//2] = chr(ord('A') + (ord(start_sequence[click_position//2]) - ord('A') + 1) % 6)
            else:
                start_sequence[(click_position+9)//2] = chr(ord('A') + (ord(start_sequence[(click_position+9)//2]) - ord('A') + 1) % 6)

    return clicks

start_sequence = input()
target_sequence = input()
min_clicks = transform_sequence(start_sequence, target_sequence)
print(min_clicks)