#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 100,000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `n` is 1, `count` is such that `5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `n` is `n_final`, `count` is greater than 5, `ans` is a list containing values from 1 to `n_final - 1`.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function reads an integer `m` from the input (where 1 ≤ m ≤ 100,000), then calculates and prints the count of integers from 1 up to the largest integer `n` such that the division of `n` by powers of 5 is still greater than or equal to `m`. It outputs the count and the list of integers that satisfy this condition, but will not process any input or return any values besides printed output.

