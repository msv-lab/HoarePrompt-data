#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, the program will have processed `t` test cases. For each test case, it will have read an integer `n` and a list `a` of `n` integers. It counts the occurrences of each integer in `a` using the list `cntl`. If `cntl[0]` is 0, it prints 0. Otherwise, it finds and prints the smallest integer `j` (from 1 to `n`) such that `cntl[j]` is less than 2, or `n` if no such `j` is found.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers where each integer `a_i` is between 0 and `n-1`. It then determines and prints the smallest integer `j` (from 1 to `n`) such that the count of `j` in the list `a` is less than 2, or `n` if no such `j` exists. If the count of 0 in the list `a` is 0, it prints 0 immediately.

