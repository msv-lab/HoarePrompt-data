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
        
    #State: The loop iterates through each test case, and for each test case, it processes the binary strings `d` and `e` of lengths `b` and `c` respectively. The variable `k` is updated based on the positions of characters in `d` within `e`. After the loop completes, `k` is printed for each test case. The initial values of `t`, `n`, and `m` remain unchanged, and the loop has no effect on the overall structure of the test cases.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads two integers `b` and `c`, followed by two binary strings `d` and `e` of lengths `b` and `c`, respectively. It then computes an integer `k` which represents the position in `d` where the substring of `d` up to that point is no longer a substring of the remaining part of `e`. If `d` is a substring of `e`, `k` will be the length of `d`. The function prints `k` for each test case. The initial values of `t`, `n`, and `m` remain unchanged, and the function does not return any values.

