#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives two integers n (2 ≤ n ≤ 10^8) and k (1 ≤ k ≤ 4n - 2) representing the size of the square grid and the minimum number of diagonals that need to have at least one colored cell, respectively.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The output state consists of a series of printed integers, each corresponding to the result of processing one test case based on the given conditions.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` representing the size of a square grid and an integer `k` representing the minimum number of diagonals that need to have at least one colored cell. For each test case, it calculates and prints the minimum number of cells that need to be colored to meet the requirement for `k` diagonals.

