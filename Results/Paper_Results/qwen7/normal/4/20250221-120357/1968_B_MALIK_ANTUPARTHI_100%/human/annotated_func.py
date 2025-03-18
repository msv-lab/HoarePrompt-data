#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2⋅10^5, and the sum of all m values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all its iterations, `a` is the total number of iterations the loop ran, `i` ranges from `0` to `a-1`, `b` remains a positive integer, `j` is equal to `2 * b - 1`, and `k` is equal to `b`. The value of `t` remains an integer such that \(1 \leq t \leq 10^4\), and the values of `d` and `e` are determined by the inputs provided during each iteration of the loop.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will have taken on every integer value from `0` to `a-1`, where `a` is the number of times the outer loop was executed. For each iteration, `b` is a positive integer, `j` will always be `2 * b - 1`, and `k` will be set to `b`. The values of `t`, `d`, and `e` will reflect the inputs given during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts integers `n` and `m`, and binary strings `a` and `b`. It calculates and prints the position `k` in string `e` where the substring `d` (derived from `a`) can be found, or indicates if it cannot be found. After processing all test cases, it outputs the results for each case.

