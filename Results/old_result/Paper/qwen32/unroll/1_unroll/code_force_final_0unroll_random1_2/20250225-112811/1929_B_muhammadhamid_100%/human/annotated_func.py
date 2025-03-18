#State of the program right berfore the function call: The function takes no explicit input arguments. However, it is expected to read input from standard input where the first line contains a single integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) representing the size of the square grid and the minimum number of diagonals that must contain at least one colored cell, respectively.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: A sequence of integers, each corresponding to the result of the calculations for each test case as described in the loop logic.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers `n` and `k`. It calculates and prints the minimum number of colored cells required to ensure that at least `k` diagonals of an `n x n` square grid contain at least one colored cell.

