#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5, representing the lengths of binary strings a and b, respectively. a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^5.
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
        
    #State: For each test case, the loop will output an integer `k` which represents the position in the binary string `d` where the loop stops. The values of `t`, `n`, and `m` remain unchanged. The binary strings `a` and `b` are not modified by the loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `m`, and two binary strings `d` and `e` of lengths `n` and `m` respectively. It reads the number of test cases `a` from the input, and for each test case, it reads `n`, `m`, `d`, and `e`. The function then searches for the position in `d` where the next character of `d` is no longer found in the remaining part of `e` starting from the current position. It outputs an integer `k` for each test case, which represents the position in `d` where the search stops. The values of `t`, `n`, and `m` remain unchanged, and the binary strings `d` and `e` are not modified by the function.

