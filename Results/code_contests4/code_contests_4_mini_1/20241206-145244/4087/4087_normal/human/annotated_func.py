#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of integers of length n+1 where each integer a_i satisfies 1 ≤ a_i ≤ n and every integer from 1 to n appears at least once in the list.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer within the range 1 ≤ n ≤ 10^5, `left` is 0, `right` is 0, `mask` is 1000000007, `pow` is a list where `pow[i]` is the factorial of `i` for `i` in range 1 to n + 1, `tmp` is `(n + 1)!`.
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer within the range 1 ≤ n ≤ 10^5; `left` is the index of the first occurrence of a duplicate element in `a` if found, otherwise 0; `right` is the index of the duplicate element in the sublist `a[x + 1:]` plus `x + 1` if found, otherwise 0; `mask` is 1000000007; `pow` is a list where `pow[i]` is the factorial of `i` for `i` in range 1 to `n + 1`; `tmp` is `(n + 1)!`.
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: `n` is within the range 1 ≤ n ≤ 10^5; `left` is an index; `right` is an index; `mask` is 1000000007; `pow` is a list of factorials; `tmp` is (n + 1)!; `i` is `n + 1`; `ans` is calculated; `x` is calculated; and the last printed output is `(ans - x) % 1000000007.
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of integers, where each integer from 1 to `n` appears at least once. It calculates and prints the difference between two combinatorial values based on the factorial of `n + 1`, the index of the first duplicate element in the list, and the index of that duplicate in the subsequent part of the list. The calculation is performed modulo `10^9 + 7`. If no duplicate is found, the function will still execute but may produce incorrect results as the indices for `left` and `right` will remain zero, leading to potential division by zero errors in the combinatorial calculations.

