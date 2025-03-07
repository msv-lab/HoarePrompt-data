#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2·10^5), m is a positive integer (1 ≤ m ≤ 10^4), a is a list of n positive integers (1 ≤ a_i ≤ 10^4), and s is a string of length n consisting of characters 'L' and 'R'.
def func_1(n, m, a, s):
    b = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2·10^5), `m` is a positive integer (1 ≤ m ≤ 10^4), `a` is a list of n positive integers (1 ≤ a_i ≤ 10^4), `s` is a string of length n consisting of characters 'L' and 'R', `b` is a list of n integers where elements are taken from `a` in the order specified by `s`, `l` is n, `r` is -1.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        
        ans.append(p)
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2·10^5), `m` is a positive integer (1 ≤ m ≤ 10^4), `a` is a list of n positive integers (1 ≤ a_i ≤ 10^4), `s` is a string of length n consisting of characters 'L' and 'R', `b` is a list of n integers where elements are taken from `a` in the order specified by `s`, `l` is n, `r` is -1, `ans` is a list of n integers where each element is the product of the corresponding element in `b` and all subsequent elements in `b`, modulo `m`, `p` is the product of all elements in `b`, modulo `m`.
    return reversed(ans)
    #The program returns a reversed list of integers, where each integer is the product of the corresponding element in `b` and all subsequent elements in `b`, modulo `m`. The length of the returned list is `n`.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (a positive integer), `m` (a positive integer), `a` (a list of `n` positive integers), and `s` (a string of length `n` consisting of characters 'L' and 'R'). It returns a reversed list of `n` integers, where each integer is the product of the corresponding element in `b` and all subsequent elements in `b`, modulo `m`. The list `b` is constructed by selecting elements from `a` in an order specified by the characters in `s` ('L' for left-to-right and 'R' for right-to-left).

