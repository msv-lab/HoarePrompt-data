#State of the program right berfore the function call: The function receives multiple test cases. Each test case is defined by two integers, n and k, where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2. The integer n represents the size of the square grid, and k represents the minimum number of diagonals that must contain at least one colored cell.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: t remains unchanged, n and k are not retained after the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers, `n` and `k`. It calculates and prints a value indicating the minimum number of colored cells required to ensure that at least `k` diagonals of an `n`-sized square grid contain at least one colored cell. After processing each test case, the function does not retain the values of `n` and `k`.

