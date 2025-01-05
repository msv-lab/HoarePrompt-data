#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100000, and a is a list of integers of length n+1 where each integer a_i satisfies 1 <= a_i <= n and every integer from 1 to n appears at least once in the list.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100000; `tmp` is the factorial of `n + 1`; `pow[i]` is the factorial of `i` for all `1 <= i <= n + 1`.
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100000; `tmp` is the factorial of `n + 1`; `pow` is defined for all indices from 0 to `n + 1`; `left` is the index of the first occurrence of a repeated element in the list `a` if such an element exists, otherwise `left` remains undefined; `right` is the index of the second occurrence of that repeated element if it exists, otherwise `right` remains undefined.
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100000; `i` is `n + 1`; `ans` is calculated as `pow[n + 1] / (pow[n + 1] * pow[0])`; `x` is dependent on the values of `left` and `right`, which may be defined or undefined; the results printed are taken modulo `mask`.
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of integers containing values from 1 to `n` (inclusive), where every integer appears at least once. It calculates the factorial of numbers from 1 to `n + 1` and identifies the first and second occurrences of any repeated element in the list. Then, it computes a specific mathematical expression based on the factorial values and the indices of the repeated element, printing the result modulo \(10^9 + 7\). The function does not explicitly return a missing integer, but rather prints computed values based on the factorials and the indices of repetitions.

