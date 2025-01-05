#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^5, and a is a list of integers of length n+1 where each integer a_i satisfies 1 <= a_i <= n and all integers from 1 to n appear at least once in the list.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 10^5, `a` is a list of integers of length `n + 1`, `left` is 0, `right` is 0, `mask` is 1000000007, `pow` is a list where `pow[i]` is the factorial of `i` for 1 <= `i` <= `n + 1`, `tmp` is the factorial of `n + 1`.
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 10^5; `left` is the index of the first occurrence of an element in list `a` that has a subsequent duplicate, or remains 0 if no such element exists; `right` is the index of that duplicate occurrence if found, or remains 0 if no duplicates exist; `i` is the value of the last index checked (which will be `n` if no duplicates are found).
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 10^5; `i` is `n + 1`; `ans` is calculated based on `pow[n + 1]`, `pow[i]`, and `pow[n + 1 - i]`; `x` is calculated based on `pow[left + n - right]`, `pow[i - 1]`, and `pow[left + n - right - i + 1]`.
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of length `n + 1`, where each integer in `a` is between 1 and `n` and all integers from 1 to `n` appear at least once. It calculates and prints a series of values based on the factorial of indices and the presence of duplicate elements in `a`. Specifically, it identifies the indices of the first occurrence and the duplicate occurrence of an element in `a`, and uses these to compute and print values derived from factorial calculations, modulated by a specific mask. The function does not return any value; instead, it prints the results directly.

