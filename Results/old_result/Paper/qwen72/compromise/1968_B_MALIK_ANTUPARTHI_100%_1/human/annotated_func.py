#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers where 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values over all test cases do not exceed 2 · 10^5.
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
        
    #State: The value of `t` remains unchanged, `n` and `m` remain unchanged, `a` is decremented to 0, and `b` and `c` are undefined after the loop, `d` and `e` are undefined after the loop, and `k` is the last value calculated within the loop for each iteration.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` and two binary strings `d` and `e` from the input. It then calculates the smallest index `k` such that the substring of `d` up to index `k` can be found in `e` starting from the current position `k`. If the substring is not found, `k` is set to the current index `j`. The function prints the value of `k` for each test case. After all test cases are processed, the value of `a` is decremented to 0, and `b`, `c`, `d`, and `e` are undefined. The function does not return any values.

