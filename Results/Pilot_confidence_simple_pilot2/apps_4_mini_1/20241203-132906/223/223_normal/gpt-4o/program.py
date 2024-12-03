import math

def is_square(x):
    root = int(math.isqrt(x))
    return root * root == x

def min_operations_to_square(n):
    n_str = str(n)
    length = len(n_str)
    min_operations = float('inf')

    # Generate all subsequences of n_str
    for i in range(1, 1 << length):
        subsequence = ''.join(n_str[j] for j in range(length) if (i & (1 << j)))
        if subsequence and is_square(int(subsequence)):
            min_operations = min(min_operations, length - len(subsequence))

    return -1 if min_operations == float('inf') else min_operations

if __name__ == "__main__":
    n = int(input().strip())
    print(min_operations_to_square(n))
