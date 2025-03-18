#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, b is a binary string of length m. The sum of all n values and the sum of all m values over all test cases do not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` and `m` are integers such that 1 ≤ n, m ≤ 2 · 10^5, `a` is an input integer, `i` is `a - 1`, `b` is the last input integer, `c` is the last input integer, `d` is the last input value, `e` is the last input value, `j` is the index at which the loop breaks or `b` if the loop completes without breaking, `k` is the index of the last element in `d` that was found in `e` plus 1, or the index at which the loop breaks if no such element is found, the sum of all `n` values and the sum of all `m` values over all test cases do not exceed 2 · 10^5.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `a` indicating the number of test cases. For each test case, it reads two integers `b` and `c`, followed by two binary strings `d` and `e` of lengths `b` and `c` respectively. The function then searches for the first occurrence of each character in `d` within the remaining part of `e` starting from the current index `k`. If a character in `d` is found in `e`, `k` is updated to the index of the found character plus one. If a character in `d` is not found in the remaining part of `e`, or if the end of `d` or `e` is reached, the function prints the current value of `k` and moves to the next test case. After processing all test cases, the function completes.

