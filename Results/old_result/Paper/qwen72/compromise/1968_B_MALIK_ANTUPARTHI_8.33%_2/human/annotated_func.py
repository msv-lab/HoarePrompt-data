#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n, m ≤ 2 · 10^5, representing the lengths of the binary strings a and b, respectively. a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values over all test cases do not exceed 2 · 10^5.
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
        
    #State: `a` is 0, `i` is `t - 1`, `b` is the last input integer, `c` is the last input integer, `d` is the last input binary string, `e` is the last input binary string, `j` is `b - 1`, and `k` is the index of the last occurrence of any `d[j]` in `e` plus 1, or `b` if no such occurrence is found or if the loop breaks due to `k` equaling `c` or `j` equaling `b - 1`.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves two binary strings `d` and `e` of lengths `b` and `c` respectively. The function outputs an integer `k` for each test case, which represents the index in `d` up to which all characters of `d` have been found in the corresponding positions of `e`, or the length of `d` if not all characters are found. After processing all test cases, the function does not return any value, but it prints the result for each test case. The final state of the program is that all test cases have been processed and their results printed.

