#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: For each test case, the variable `c` will hold the count of elements in the list `l` that satisfy the conditions within the inner loop. The values of `t`, `n`, and `a` will remain unchanged as they are re-initialized for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers. It then identifies two elements `a` and `b` from the list `l` and counts the number of elements in `l` that satisfy certain conditions relative to `a` and `b`. The function prints the count `c` for each test case. The function does not return any value. The variables `t`, `n`, and `l` are re-initialized for each test case, so their values do not persist across test cases.

