#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: For each test case, the loop prints the number of elements in the list `l` that are greater than both the smallest and the second smallest elements found in `l`. The variables `t`, `n`, and `a` (the list) remain unchanged, while `a` and `b` (the smallest and second smallest elements) and `c` (the count) are reset and updated for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `l`. It then processes the list to count the number of elements that are greater than both the smallest and the second smallest elements in the list. The function prints this count for each test case. The variables `t`, `n`, and `l` remain unchanged after the function concludes, while the internal variables `a`, `b`, and `c` are reset and updated for each test case.

