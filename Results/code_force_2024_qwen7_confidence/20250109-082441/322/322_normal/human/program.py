import sys
import random

# Function to query Alice
def query(t, l, r):
    print(f"? {t} {l} {r}")
    sys.stdout.flush()
    return int(input().strip())

# Function to print the answer
def print_answer(ans):
    print(f"! {ans}")
    sys.stdout.flush()
    input()  # Read Bob's response (normally 1)

# Function to perform binary search to find MEX
def find_mex(n, u, v):
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if query(1, u + 1, mid + 1):
            r = mid
        else:
            l = mid + 1
    return l

# Function to shuffle array a
def shuffle_array(a):
    n = len(a)
    for i in range(n):
        j = random.randint(i, n - 1)
        a[i], a[j] = a[j], a[i]

# Main function
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, q = map(int, input().split())  # Number of nodes and rounds
        adj_list = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj_list[u - 1].append(v - 1)
            adj_list[v - 1].append(u - 1)

        # Generate two random permutations
        p1 = list(range(1, n + 1))
        p2 = list(range(1, n + 1))
        shuffle_array(p1)
        shuffle_array(p2)

        print(*p1)
        sys.stdout.flush()
        print(*p2)
        sys.stdout.flush()

        # Process each round
        for _ in range(q):
            u, v = map(int, input().split())  # Nodes for the round
            u -= 1
            v -= 1
            mex = find_mex(n, u, v)
            print_answer(mex)

# Execute main function
if __name__ == "__main__":
    main()