def draw_bracket_sequence(n, sequence):
    levels = []
    current_level = 0
    for char in sequence:
        if char == '[':
            current_level += 1
            while len(levels) < current_level:
                levels.append(0)
            levels[current_level - 1] += 1
        else:
            levels[current_level - 1] -= 1
            if levels[current_level - 1] == 0:
                levels.pop()
            current_level -= 1

    max_level = len(levels)
    drawing = [[' ' for _ in range(2 * n)] for _ in range(2 * max_level + 1)]

    current_level = 0
    pos = 0
    for char in sequence:
        if char == '[':
            drawing[current_level][pos] = '+'
            drawing[2 * max_level - current_level][pos] = '+'
            drawing[current_level][pos + 1] = '-'
            drawing[2 * max_level - current_level][pos + 1] = '-'
            drawing[current_level + 1][pos] = '|'
            drawing[2 * max_level - current_level - 1][pos] = '|'
            current_level += 1
            pos += 1
        else:
            current_level -= 1
            drawing[current_level][pos] = '-'
            drawing[2 * max_level - current_level][pos] = '-'
            drawing[current_level][pos - 1] = '+'
            drawing[2 * max_level - current_level][pos - 1] = '+'
            drawing[current_level + 1][pos - 1] = '|'
            drawing[2 * max_level - current_level - 1][pos - 1] = '|'
            pos += 1
            while pos < 2 * n and sequence[pos] == ']':
                pos += 1
            pos -= 1

    for row in drawing:
        print(''.join(row))

if __name__ == "__main__":
    n = int(input())
    sequence = input().strip()
    draw_bracket_sequence(n, sequence)
