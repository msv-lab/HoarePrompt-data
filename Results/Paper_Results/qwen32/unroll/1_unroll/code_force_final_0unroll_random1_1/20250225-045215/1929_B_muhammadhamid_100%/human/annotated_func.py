#State of the program right berfore the function call: The function will receive multiple test cases. Each test case consists of two integers, n and k, where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2. The integer n represents the size of the square grid, and k represents the minimum number of diagonals that must contain at least one colored cell.
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
        
    #State: The function will output the number of colored cells needed for each test case based on the given conditions. For each test case, if k is 1, it outputs 1. If k is less than or equal to 2 * (n + (n - 2)), it outputs the ceiling of k divided by 2. Otherwise, it outputs k divided by 2 plus 1. The state of variables not involved in the loop remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers, `n` and `k`. Here, `n` represents the size of a square grid, and `k` is the minimum number of diagonals that must contain at least one colored cell. For each test case, the function calculates and outputs the minimum number of colored cells required to meet the condition on `k`.

