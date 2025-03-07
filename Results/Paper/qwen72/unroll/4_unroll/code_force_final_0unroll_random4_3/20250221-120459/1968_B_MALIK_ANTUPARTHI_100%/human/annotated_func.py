#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n, m ≤ 2 · 10^5, representing the lengths of binary strings a and b, respectively. a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^5.
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
        
    #State: The loop will print the index `k` for each test case, where `k` is the position in string `d` up to which a matching substring from `e` has been found. The state of `t`, `n`, and `m` remains unchanged. The values of `a`, `b`, `c`, `d`, and `e` are updated for each iteration of the loop, but their final values after the loop depends on the input provided during each test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, and two binary strings `d` and `e` of lengths `n` and `m` respectively. The function then processes these strings to find the longest prefix of `d` that is a substring of `e`, and prints the length of this prefix. The state of `t` remains unchanged, but the values of `n`, `m`, `d`, and `e` are updated for each test case. After processing all test cases, the function concludes without returning any value.

