#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values over all test cases do not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `m` are integers such that 1 ≤ n, m ≤ 2 · 10^5, `a` is an integer greater than 0, the sum of all n values and the sum of all m values over all test cases do not exceed 2 · 10^5, `i` is `a - 1`, `b` is an integer greater than 0, `c` is an integer, `d` is an input string, `e` is an input string, `j` is the index where the loop was broken or `b` if the loop completed, and `k` is the last updated value of `k` based on the loop's execution.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` and two binary strings `d` and `e`. It then processes these strings to find the index `k` where the substring of `d` up to `k` can be found in `e` in the same order, but not necessarily consecutively. The function prints the value of `k` for each test case. After processing all test cases, the function concludes, and the state of the program is such that `a` is the number of test cases, `i` is `a - 1`, `b` is the last read integer representing the length of the binary string `d`, `c` is the last read integer, `d` is the last read binary string, `e` is the last read binary string, and `k` is the last computed index.

