#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, and a_i are integers where 1 <= a_i <= n. Each of the integers 1,...,n appears in the sequence.**
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
        
    #State of the program after the  for loop has been executed: `n` is incremented by 1, `right` remains 0, `mask` is 10^9 + 7, `pow` contains n+2 zeros with each element representing the product of all numbers from 1 to the corresponding index, `tmp` is the product of all numbers from 1 to n+2
    for i in range(0, n + 1):
        x = a.index(a[i])
        
        if a[i] in a[x + 1:]:
            left = i
            right = a[x + 1:].index(a[i]) + x + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `right` is updated based on the calculation `a[x + 1:].index(a[i]) + x + 1`, `mask` remains at 10^9 + 7, `pow` contains n+3 zeros with each element representing the product of all numbers from 1 to the corresponding index, `tmp` is the product of all numbers from 1 to n+3, `i` is n+2, `x` is the index of the first occurrence of the element `a[i]` in the list `a`, `left` is assigned the value of `i`. The loop executes until it finds the first repeated element in the list `a`, updating `right` accordingly, and then terminates.
    for i in range(1, n + 2):
        ans = pow[n + 1] / (pow[i] * pow[n + 1 - i])
        
        x = pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1])
        
        print(ans - x) % mask
        
    #State of the program after the  for loop has been executed: All variables maintain their values as described in the initial state, and the loop does not affect the values of any variables directly.
#Overall this is what the function does:The function `func` reads an integer `n` and a sequence of integers `a`. It then performs some calculations on the sequence `a` based on specific conditions. However, the exact operation and expected output of the function are not clearly defined in the code. The function iterates through the sequence to find the first repeated element and computes some values using mathematical operations without a clear purpose. The function lacks a specific functionality description due to the ambiguity in the code implementation.

