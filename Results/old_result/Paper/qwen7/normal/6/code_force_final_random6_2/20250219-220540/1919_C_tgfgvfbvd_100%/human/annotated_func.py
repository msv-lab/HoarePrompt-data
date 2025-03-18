#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, `x` will be equal to `n-1`, `a` will be the minimum value found in the list `l`, and `b` will be the second smallest value found in the list `l`. The variable `c` will be the count of elements in `l` that are larger than both `a` and `b`. The value of `n` will remain unchanged as it was initially provided as input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. For each test case, it finds the minimum and second smallest values in the list and counts how many elements are larger than both of these values. The function prints this count for each test case.

