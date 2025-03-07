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
        
    #State: `b` must be greater than 0, `i` is `a`, `a` remains the same, `d` is an input string, `e` is an input string, `k` is the final value determined by the loop based on the conditions provided, and `j` is `b - 1`.
#Overall this is what the function does:The function processes multiple test cases, each involving two binary strings \(a\) and \(b\) of specified lengths \(n\) and \(m\). For each test case, it finds the smallest index \(k\) in string \(b\) where a substring of \(b\) of length equal to the length of \(a\) can be found. If no such substring exists, it returns the length of \(b\). The function prints the value of \(k\) for each test case and does not return any value explicitly.

