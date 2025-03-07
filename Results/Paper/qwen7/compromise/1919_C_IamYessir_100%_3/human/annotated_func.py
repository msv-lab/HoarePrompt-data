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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to the length of `b` minus 1, `s` will be the count of elements in `b` where each element is greater than its predecessor, `n` will be the total number of iterations executed (which is `len(b) - 1`), `x` will be reassigned to the last element of list `b`, `y` will still be `float('inf')`, and lists `a` and `b` will contain elements based on the conditions involving `x` and `lit[i]` for list `a`, and `y` and `lit[i]` for list `b`. The list `lit` will remain unchanged.
    #
    #In simpler terms, after the loop finishes executing all iterations:
    #- `i` will be the index of the last element in `b`.
    #- `s` will count how many times an element in `b` is greater than the previous element.
    #- `n` will be the number of iterations, which is `len(b) - 1`.
    #- `x` will be the last element of `b`.
    #- `y` remains `float('inf')`.
    #- Lists `a` and `b` will be filled according to the conditions in the loop, with `a` containing elements based on comparisons with `x` and `b` based on comparisons with `y`.
    #- The original list `lit` will not change.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. For each test case, it divides the list into two sublists, \( a \) and \( b \), based on certain conditions. It then counts the number of times an element in sublist \( b \) is greater than the previous element. The function prints this count for each test case.

