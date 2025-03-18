#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives two integers n (2 ≤ n ≤ 10^8) and k (1 ≤ k ≤ 4n - 2) where n is the size of the square grid and k is the minimum number of diagonals that should have at least one colored cell.
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
        
    #State: The function will have printed the results for each test case based on the provided logic. The value of t will have been decremented to 0 as all test cases have been processed. The variables n and k will hold the values of the last test case processed, but they are not retained outside the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by the size of a square grid `n` and a minimum number of diagonals `k` that should have at least one colored cell. For each test case, it calculates and prints the number of diagonals that need to be colored to meet the requirement.

