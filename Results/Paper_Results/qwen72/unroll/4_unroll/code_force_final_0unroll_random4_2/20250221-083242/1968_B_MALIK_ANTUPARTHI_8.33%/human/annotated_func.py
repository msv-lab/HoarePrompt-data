#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers for each test case such that 1 ≤ n, m ≤ 2 · 10^5, a is a binary string of length n, and b is a binary string of length m. The sum of all n values and the sum of all m values across all test cases do not exceed 2 · 10^5.
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
        
    #State: The value of `t` remains unchanged as it is not modified within the loop. The loop iterates `a` times, and for each iteration, `b`, `c`, `d`, and `e` are updated based on the input. After each iteration, `k` is printed, and its value is determined by the logic within the inner loop. The values of `n` and `m` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, representing the number of test cases. For each test case, it reads two integers `b` and `c`, followed by two binary strings `d` and `e` of lengths `b` and `c` respectively. It then processes these strings to find the smallest index `k` such that the substring of `d` up to index `k` can be found in `e`. If the entire string `d` is found in `e`, `k` will be the length of `d`. The function prints the value of `k` for each test case. The function does not return any value, and it does not modify the initial state of `t`, `n`, or `m` as they are not used or modified within the function.

