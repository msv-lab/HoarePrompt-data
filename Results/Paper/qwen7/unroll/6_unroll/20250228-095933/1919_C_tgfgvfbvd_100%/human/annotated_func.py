#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. After executing the loop, the variable c contains the number of times the value of `a` or `b` is updated in each test case.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( n \) and a list of \( n \) integers. It calculates and prints the number of times the values of \( a \) or \( b \) are updated within each test case. The initial values of \( a \) and \( b \) are set to infinity, and during the iteration over the list, \( a \) and \( b \) are updated based on the conditions provided. The function outputs the count of updates for each test case.

