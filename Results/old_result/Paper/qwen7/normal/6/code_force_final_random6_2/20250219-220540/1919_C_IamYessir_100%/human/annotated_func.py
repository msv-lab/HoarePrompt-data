#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n such that 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `i` will be equal to `len(b) - 1`, `n` will be the value it was initialized to (which is less than or equal to 2 * 10^5), and `s` will be the total count of elements in `b` where each element is greater than the previous one. The lists `a` and `b` will contain the elements from `lit` that satisfy the conditions specified in the loop, and `cp` will retain its value from the final iteration of the loop or its initial state if it was not modified by the loop.
    #
    #In simpler terms, after the loop completes, `i` will be the last index of list `b`, `n` will be the number of elements processed, `s` will count how many times an element in `b` is larger than the previous element, and the lists `a` and `b` will hold the sorted elements based on specific conditions, with `cp` retaining its final value.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers. It sorts these integers into two lists, `a` and `b`, based on specific conditions. For each test case, it counts how many times an element in list `b` is greater than the previous element. Finally, it prints the total count of such instances across all test cases.

