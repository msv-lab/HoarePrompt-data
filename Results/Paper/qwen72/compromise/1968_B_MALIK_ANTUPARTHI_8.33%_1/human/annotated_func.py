#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers for each test case where 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: The value of `t` remains unchanged, and the loop prints a value `k` for each iteration of the outer loop. The values of `n` and `m` remain unchanged, and the values of `a`, `b`, `c`, `d`, and `e` are consumed and reset for each iteration of the outer loop.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `m`, followed by two binary strings `a` and `b` of lengths `n` and `m`, respectively. The function then processes these strings to find the smallest index `k` such that the substring `a[:k+1]` is a subsequence of `b`. It prints this index `k` for each test case. The function does not return any value, and the values of `n` and `m` remain unchanged for each test case. The input variables `a`, `b`, `c`, `d`, and `e` are consumed and reset for each iteration of the outer loop.

