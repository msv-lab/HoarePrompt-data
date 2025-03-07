#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^5.
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
        
    #State: The value of `t` remains unchanged, `n` and `m` remain unchanged, `a` is decremented by the number of iterations the loop has executed, and `b`, `c`, `d`, `e`, and `k` are modified within each iteration but their final values after the loop are not predictable without specific inputs.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` and two binary strings `d` and `e` from the input. It then processes these inputs to find the smallest index `k` such that the substring `d[:j+1]` (for some `j` in the range `[0, b-1]`) is a subsequence of `e[k:]`. If such a subsequence is found, it prints the index `k`. If no such subsequence is found, it prints the index of the last character processed in `d`. The function does not return any value. After the function concludes, the value of `a` is decremented by the number of test cases processed, and the values of `b`, `c`, `d`, `e`, and `k` are modified within each iteration but their final values are not predictable without specific inputs. The values of `t`, `n`, and `m` remain unchanged.

