#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to the length of `b`, `b` will contain all elements from `lit` that are strictly greater than the last element of `a`, and `s` will be the count of elements in `b` where each element is greater than its predecessor.
    #
    #In natural language: The final state of the loop will have `i` equal to the length of `b`, indicating that the loop has iterated through all elements of `b`. The list `b` will consist of all elements from `lit` that are strictly greater than the last element of `a`. The variable `s` will hold the total count of elements in `b` where each element is greater than the previous one.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( n \) and a list of \( n \) integers. For each test case, it identifies two lists: `a` and `b`. List `a` contains the smallest element from the input list followed by elements from the input list that are greater than the last element added to `a`. List `b` contains the remaining elements from the input list that are not in `a`. The function then counts the number of times an element in `b` is greater than the preceding element and prints this count for each test case.

