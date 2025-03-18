#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a and b are binary strings of lengths n and m respectively. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and similarly, the sum of all m values does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an input integer, b and c are integers obtained from user input, d and e are strings obtained from user input, k is an integer initialized to 0 and updated within the loop based on conditions.
    #
    #In each iteration of the outer loop (controlled by `i`), the value of `k` is updated based on the comparison between characters of strings `d` and `e`. The final value of `k` for each iteration is printed. The initial values of `b`, `c`, `d`, `e`, and `k` are determined by user input during each iteration of the outer loop. The value of `a` controls the number of times the outer loop runs. After all iterations of the outer loop have finished, the final state of `k` for each iteration will be the last printed value of `k` for that particular iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two binary strings \(d\) and \(e\), and determines the smallest index \(k\) in string \(d\) such that the substring of \(d\) starting from index \(k\) matches any substring of \(e\). It prints \(k\) for each test case. The function effectively finds the earliest matching position of any substring of \(d\) within \(e\) for each test case.

