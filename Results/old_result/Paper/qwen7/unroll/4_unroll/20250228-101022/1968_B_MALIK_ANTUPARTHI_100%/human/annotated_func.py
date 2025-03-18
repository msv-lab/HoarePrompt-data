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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an integer obtained from input, each iteration of the outer loop modifies variable `k` based on the conditions provided within the nested loop. After all iterations of the outer loop have finished, `k` will hold the final value determined by the last execution of the inner loop for each `i` in the range of `a`. The exact value of `k` depends on the inputs provided during each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t (1 ≤ t ≤ 10^4), two integers n and m (1 ≤ n, m ≤ 2⋅10^5), and two binary strings a and b (lengths n and m respectively). For each test case, it finds the position k in string b where a substring of a matches a subsequence of b, and prints the final value of k for each test case. The function does not return any value but outputs the results for each test case.

