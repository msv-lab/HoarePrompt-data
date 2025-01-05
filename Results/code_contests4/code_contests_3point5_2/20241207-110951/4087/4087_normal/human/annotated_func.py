#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, and a_i is an integer such that 1 <= a_i <= n. Each integer from 1 to n appears in the sequence.**
def func():
    n = int(raw_input())
    a = map(int, re.split('\\s', raw_input()))
    left = 0
    right = 0
    mask = 10 ** 9 + 7
    pow = [0] * n + 2
    tmp = 1
    for i in range(1, n + 2):
        tmp *= i
        
        pow[i] = tmp
        
    #State of the program after the  for loop has been executed: Output State: `n` is an input integer, `left` is 0, `right` is 0, `mask` is 1000000007, `pow` is a list of size `n + 2` filled with zeros except for `pow[i]` which is assigned the value of the factorial of `i`, `tmp` is the result of multiplying all integers from 1 to `n + 2`
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `left` is the index of the first occurrence of a value in the list `a` that is repeated later in the list, `right` is the index of the second occurrence of that value in the list after the first occurrence, `mask` is 1000000007, `pow` is a list of size `n + 2` filled with zeros except for `pow[i]` which is assigned the value of the factorial of `i`, `tmp` is the result of multiplying all integers from 1 to `n + 2`
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: Output State: `n` is input integer, `left` is the index of the first occurrence of a value in the list `a` that is repeated later in the list, `right` is the index of the second occurrence of that value in the list after the first occurrence, `mask` is 1000000007, `pow` is a list of size `n + 2` filled with factorials of 0 to `n + 1`, `tmp` is the result of multiplying all integers from 1 to `n + 2`, for the loop to execute `n` is greater than or equal to 1. The loop performs calculations to obtain `ans` and `x` using specific formulas and prints the result of `(ans - x) % mask` for each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `n` followed by a sequence of integers. It then calculates specific values based on the input sequence and prints the results. The function does not accept any parameters explicitly but processes the input sequence to perform calculations and output results.

