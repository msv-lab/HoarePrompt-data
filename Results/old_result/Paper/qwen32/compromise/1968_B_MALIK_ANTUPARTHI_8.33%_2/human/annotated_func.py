#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5. a and b are binary strings of length n and m, respectively. The sum of all n values across test cases does not exceed 2 * 10^5, and the sum of all m values across test cases does not exceed 2 * 10^5.
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
        
    #State: `k` is the final value determined by the last iteration, `i` is `a`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, and two binary strings `a` and `b` of lengths `n` and `m`, respectively. It then determines the maximum length of the prefix of string `a` that can be matched with a subsequence in string `b` without exceeding the length `m`. The function prints this length for each test case.

