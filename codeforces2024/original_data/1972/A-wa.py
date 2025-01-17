def solve(a, b):
    num_new_problems = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            num_new_problems += a[i] - b[i]

    return num_new_problems