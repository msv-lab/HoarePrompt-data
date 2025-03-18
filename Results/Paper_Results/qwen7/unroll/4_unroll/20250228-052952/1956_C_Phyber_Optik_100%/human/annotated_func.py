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
        
    #State: Output State: The output consists of multiple lines for each iteration of the outer loop. For each iteration, it prints the value of `sum` and `n + n`, followed by two blocks of lines. Each block contains `n` lines where the first column alternates between 1 and 2, the second column decreases from `n` to 1, and the third column is a range from 1 to `n`.
    #
    #For each value of `t` (1 ≤ `t` ≤ 500), the loop will execute `t` times, producing the described output for each `n` provided in the input.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 500) and an integer `t` (1 ≤ t ≤ 500). It calculates a sum based on `n` using a specific formula and prints this sum along with `n + n`. Additionally, it prints two blocks of lines, each containing `n` lines. In these blocks, the first column alternates between 1 and 2, the second column decreases from `n` to 1, and the third column is a range from 1 to `n`. This process repeats `t` times for each test case.

