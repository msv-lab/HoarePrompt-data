#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n and m are integers where 1 <= n, m <= 2 * 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 * 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: t remains an integer where 1 <= t <= 10^4, n and m remain integers where 1 <= n, m <= 2 * 10^5, a is an integer input, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 * 10^5. The loop prints the value of k for each iteration of the outer loop, where k is the index in the string d up to which the characters of d can be found in e in the same order.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c`, followed by two binary strings `d` and `e` of lengths `b` and `c` respectively. The function then processes these strings to find the index `k` in string `d` up to which the characters of `d` can be found in `e` in the same order. It prints the value of `k` for each test case. The function does not return any value. After the function concludes, `t` remains an integer where 1 <= t <= 10^4, `n` and `m` remain integers where 1 <= n, m <= 2 * 10^5, and the sum of all `n` values and the sum of all `m` values across all test cases do not exceed 2 * 10^5. The input variables `a`, `b`, `c`, `d`, and `e` are consumed and no longer available.

