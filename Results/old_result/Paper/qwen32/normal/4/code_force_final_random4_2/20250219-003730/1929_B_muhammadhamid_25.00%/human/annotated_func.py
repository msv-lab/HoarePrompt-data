#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives two integers n (2 ≤ n ≤ 10^8) and k (1 ≤ k ≤ 4n - 2) where n is the size of the square grid and k is the minimum number of diagonals that must contain at least one colored cell.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop has executed `t` times, and for each test case, the appropriate result based on the values of `n` and `k` has been printed. The variable `t` is now 0, and no further test cases remain to be processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid size `n` and a requirement `k`. For each test case, it calculates and prints the minimum number of cells that need to be colored to ensure that at least `k` diagonals of the `n x n` grid contain at least one colored cell.

