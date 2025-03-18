#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n is a positive integer (1 ≤ n ≤ 2·10^5) for each test case, and a is a list of n integers (1 ≤ a_i ≤ n).
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
        
    #State: The loop will print the value of `c` for each test case, which represents the number of times a number in the list `l` was found to be greater than both `a` and `b` and satisfied the given conditions. The variables `t`, `n`, `l`, `a`, `b`, `c`, and `y` will be reset for each test case, and the loop will execute `t` times, processing each list `l` of length `n` independently. After all iterations, the final state of `t`, `n`, `l`, `a`, `b`, `c`, and `y` will be undefined for the next test case, but the output will be the printed values of `c` for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer `n` and a list `l` of `n` integers. For each test case, it identifies the number of elements in `l` that are greater than both the first element of `l` and a subsequent element found to be greater than its predecessor. The function prints this count for each test case. The variables `t`, `n`, `l`, `a`, `b`, `c`, and `y` are reset for each test case, and the function does not return any value. The final state of these variables is undefined after the function concludes, but the output consists of the printed values of `c` for each test case.

