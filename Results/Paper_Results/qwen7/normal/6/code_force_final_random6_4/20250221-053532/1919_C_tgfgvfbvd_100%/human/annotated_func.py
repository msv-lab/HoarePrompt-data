#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `a` will be the minimum value in the list `l`, and `b` will be the second smallest value in the list `l`. The variable `c` will be equal to the count of elements in `l` that are greater than both `a` and `b`. The variable `x` will be `n`, and it will not affect the final values of `a`, `b`, or `c`.
    #
    #This means that after processing all elements in the list `l`, `a` and `b` will hold the smallest and second smallest values from the list, respectively, and `c` will count how many numbers in the list are larger than these two smallest values.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( n \) and a list of \( n \) integers. For each test case, it finds the smallest and second smallest numbers in the list and counts how many numbers in the list are greater than these two smallest numbers. The function prints the count for each test case and does not return any value.

