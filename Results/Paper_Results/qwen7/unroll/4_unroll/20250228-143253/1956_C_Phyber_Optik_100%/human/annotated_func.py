#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: Output State: t is an input integer, 1 ≤ t ≤ 500. After executing the loop, for each input value of n:
    #- The sum is calculated based on the given formula and printed along with n + n.
    #- Two blocks of output are printed for each value of n, each block containing n lines of output where the first column alternates between 1 and 2, the second column decreases from n to 1, and the third column contains the range of numbers from 1 to n.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates a sum based on a specific formula and prints the sum along with `n + n`. Additionally, it prints two blocks of output for each value of `n`, where the first column alternates between 1 and 2, the second column decreases from `n` to 1, and the third column contains the range of numbers from 1 to `n`.

