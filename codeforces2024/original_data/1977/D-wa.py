def xorificator(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    flipped = [False] * rows
    result = [0] * rows
    count = 0

    for j in range(cols):
        indices = []
        for i in range(rows):
            if matrix[i][j] == '1':
                indices.append(i)
        if len(indices) == 1 and not flipped[indices[0]]:
            flipped[indices[0]] = True
            count += 1
        elif len(indices) > 1:
            for idx in indices:
                if not flipped[idx]:
                    flipped[idx] = True
                    count += 1
                    break
                else:
                    matrix[idx] = ''.join('1' if c=='0' else '0' for c in matrix[idx])
                    if not flipped[idx]:
                        flipped[idx] = True
                        count += 1
                        break

    print(count)
    print(''.join('1' if f else '0' for f in flipped))

# Test Cases
testcases = int(input())
for _ in range(testcases):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    xorificator(matrix)