
def perform_action(N, t, A):
    if t == 1:
        print(7)
    elif t == 2:
        if A[0] > A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:
            print("Smaller")
    elif t == 3:
        median = sorted([A[0], A[1], A[2]])[1]
        print(median)
    elif t == 4:
        total_sum = sum(A)
        print(total_sum)
    elif t == 5:
        even_sum = sum([num for num in A if num % 2 == 0])
        print(even_sum)
    elif t == 6:
        char_sequence = ""
        for num in A:
            char_sequence += chr(num % 26 + 97)
        print(char_sequence)
    elif t == 7:
        current_index = 0
        visited = set()
        is_infinite_loop = False
        while current_index >= 0 and current_index < N:
            if current_index in visited:
                is_infinite_loop = True
                break
            visited.add(current_index)
            if current_index == N - 1:
                print("Done")
                return
            current_index = A[current_index]
        if is_infinite_loop:
            print("Cyclic")
        else:
            print("Out")

# Read input values
N, t = map(int, input().split())
A = list(map(int, input().split()))

# Perform the required action
perform_action(N, t, A)