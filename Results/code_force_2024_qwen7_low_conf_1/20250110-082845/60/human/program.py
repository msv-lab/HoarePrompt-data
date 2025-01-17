def find_modular_sequence(n, x, y, s):
    # Initialize the sequence with the first element
    sequence = [x]
    current_sum = x

    # Calculate the sequence
    for i in range(1, n):
        # Check if adding y or taking mod y will help reach the sum
        if current_sum + y <= s and (s - current_sum - y) % y == 0:
            sequence.append(sequence[-1] + y)
            current_sum += y
        else:
            sequence.append(sequence[-1] % y)
            current_sum += sequence[-1]

        # If the current sum exceeds the required sum, it's not possible
        if current_sum > s:
            return None

    # Check if the final sum matches the required sum
    if current_sum == s:
        return sequence
    else:
        return None

# Input reading
t = int(input())
for _ in range(t):
    n, x, y, s = map(int, input().split())
    result = find_modular_sequence(n, x, y, s)
    if result:
        print("Yes")
        print(" ".join(map(str, result)))
    else:
        print("No")