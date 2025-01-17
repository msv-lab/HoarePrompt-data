def find_solution(a, b, n):
    for x in range(n // a + 1):
        remainder = n - a * x
        if remainder % b == 0:
            y = remainder // b
            return (x, y)
    return None

# Testing the function with the provided test cases
assert find_solution(2, 3, 7) == (2, 1)
assert find_solution(4, 2, 7) == None
assert find_solution(1, 13, 17) == (4, 1)
