#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [], []
        
        cp = 0
        
        for i in range(0, n):
            if len(a) == 0:
                x = float('inf')
            else:
                x = a[-1]
            if len(b) == 0:
                y = float('inf')
            else:
                y = b[-1]
            if x > y:
                if y >= lit[i]:
                    b.append(lit[i])
                elif lit[i] > x:
                    b.append(lit[i])
                elif x >= lit[i] and lit[i] > y:
                    a.append(lit[i])
            elif x == y:
                a.append(lit[i])
            elif x < y:
                if x >= lit[i]:
                    a.append(lit[i])
                elif lit[i] > y:
                    a.append(lit[i])
                elif y >= lit[i] and lit[i] > x:
                    b.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to `len(b)`, indicating that every index from 1 to `len(b)-1` has been checked. The variable `s` will hold the total count of times the condition `b[i] > b[i - 1]` was true during the loop's execution. The list `a` will contain elements that were not appended to `b` based on the given conditions. The list `b` will contain elements that were appended to it according to the conditions inside the loop. The value of `x` will be the last element of list `a` (or infinity if `a` is empty), and `y` will be the last element of list `b` (or infinity if `b` is empty). The variable `n` will remain unchanged, holding the original value provided at the start of the loop, and `lit` will be the list of integers processed by the loop.
    #
    #In summary, `s` represents the number of increasing pairs in list `b`, while `a` and `b` are populated based on specific comparison conditions against the input list `lit`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers. For each test case, it populates two lists, `a` and `b`, based on specific comparison conditions against the input list `lit`. It then counts the number of increasing pairs in list `b` and prints this count. The function does not return any value but prints the result for each test case.

