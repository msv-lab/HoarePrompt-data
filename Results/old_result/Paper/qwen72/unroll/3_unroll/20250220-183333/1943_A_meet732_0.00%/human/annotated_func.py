#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. The total number of test cases t is a positive integer (1 ≤ t ≤ 2 · 10^4), and the sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The loop has finished executing all test cases. For each test case, the output is the smallest index j such that cntl[j] < 2, or 0 if cntl[0] is not zero. The variables `t`, `n`, and `a` are not affected by the loop and retain their initial values. The list `cntl` is updated to reflect the count of each integer in the list `a` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then counts the occurrences of each integer in `a` and outputs the smallest index `j` such that the count of `j` is less than 2, or 0 if the count of 0 is zero. After processing all test cases, the function does not modify the input variables `t`, `n`, or `a`. The list `cntl` is used internally to store the counts and is reset for each test case.

