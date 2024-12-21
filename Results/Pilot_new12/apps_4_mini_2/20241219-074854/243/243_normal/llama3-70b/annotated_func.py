#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 100000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `count` is the smallest integer such that `n` divided by 5 raised to the power of `count` is less than `m`, `n` is 1, and if `m` was initially greater than 0, the loop will execute until `count` is such that `n // 5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `count` is the smallest integer such that `1` divided by `5` raised to the power of `count` is less than `m`, `n` is equal to the final value before the loop condition failed, and `ans` contains all values from 1 up to that final value of `n - 1`. If the loop executes at least once, then `m` must be greater than 0.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function takes a positive integer input `m` (where 1 ≤ m ≤ 100000) and performs two primary tasks. Firstly, it calculates the smallest integer `count` such that \(1 / 5^{count} < m\). In practical terms, it finds the highest power of 5 that divides into `m`. Secondly, it constructs a list `ans` that includes all integers from 1 up to the value where \(n / 5^{count} < m\). The final output of the function is the length of this list `ans` followed by the elements of `ans` printed in a single line. Thus, the function effectively retains the sequence of integers up to a limit determined by the relationship of `m` with the powers of 5, and informs the user of how many such integers exist, along with listing them. Note that the code assumes proper input and does not handle any edge cases for invalid input types.

