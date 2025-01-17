import sys, os, getpass

# Read input data
sys.stdin = open(os.path.join(os.getcwd(), 'a.txt'), 'r') if getpass.getuser() == '4a' else sys.stdin
IM = lambda: [[int(a) for a in l.split()] for l in sys.stdin]

A = IM()
print(A) if getpass.getuser() == '4a' else None

def solution(A):
    def f(arr):
        n, k, p = arr
        # Initialize dp arrays
        dp = [[0] * (k + 1) for _ in range(2)]
        dp[0][0] = 1  # Base case: one way to have an empty array with sum 0
        prev = [[0] * (k + 1) for _ in range(2)]

        # Iterate over each possible length of the array
        for i in range(1, n + 2):
            ndp = [[0] * (k + 1) for _ in range(2)]
            psum = [0, 0]  # Prefix sums for efficient calculation
            for j in range(2):
                for x in range(k + 1):
                    psum[j] += dp[j][x]
                    psum[j] %= p  # Ensure values are within modulo p
            for j in range(2):
                a, b = 0, 0
                for x in reversed(range(k + 1)):
                    ndp[j][x] += psum[j]
                    ndp[j][x] += b
                    ndp[j][x] %= p
                    a += prev[j ^ 1][k - x]
                    a %= p
                    b += a
                    b %= p
            prev = dp
            dp = ndp

        # Calculate the result for this test case
        return (dp[0][0] - dp[1][0] + p) % p

    # Process each test case
    for i in range(1, len(A)):
        s = A[i]
        print(f(s))

solution(A)