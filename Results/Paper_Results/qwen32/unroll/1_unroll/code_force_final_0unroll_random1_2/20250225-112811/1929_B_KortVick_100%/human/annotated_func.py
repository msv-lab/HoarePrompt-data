#State of the program right berfore the function call: The function receives input through standard input. The first line contains a single integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) where n is the size of the square grid and k is the minimum number of diagonals that must contain at least one colored cell.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: A series of printed numbers, one for each test case, where each number is either `k // 2 + 1` if `4 * n - 2 == k`, or `ceil(k / 2)` otherwise.
#Overall this is what the function does:The function reads a number of test cases from standard input. For each test case, it reads two integers, `n` and `k`. It then computes and prints a result based on the value of `k` relative to `4 * n - 2`: if `k` equals `4 * n - 2`, it prints `k // 2 + 1`; otherwise, it prints the ceiling of `k / 2`.

