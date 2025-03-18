#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, representing the number of test cases. For each test case, n and m are integers where 1 <= n, m <= 2 * 10^5, representing the lengths of binary strings a and b, respectively. a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 * 10^5.
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
        
    #State: `t` is an integer where 1 <= t <= 10^4, `n` is an integer where 1 <= n <= 2 * 10^5, `m` is an integer where 1 <= m <= 2 * 10^5, `a` is an input integer that must be greater than 0, `b` is an integer that must be greater than 0, `c` is an integer, `i` is `a - 1`, `d` is the input value for the last iteration, `e` is the input value for the last iteration, `j` is `b` if the loop completed, otherwise it is the index at which the loop broke. `k` is the final value of `k` after the loop completes or breaks.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` (representing the lengths of two binary strings `d` and `e`), and then reads the binary strings `d` and `e` from the input. The function then processes these strings to find the index `k` where the characters of `d` can be matched in `e` in the same order, but not necessarily consecutively. After processing, it prints the value of `k` for each test case. The function does not return any value; it only prints the results. After the function concludes, the input variables `a`, `b`, `c`, `d`, and `e` are no longer relevant, and `i` is `a - 1`. The function is designed to handle up to `10^4` test cases, with the sum of all `n` and `m` values across all test cases not exceeding `2 * 10^5`.

