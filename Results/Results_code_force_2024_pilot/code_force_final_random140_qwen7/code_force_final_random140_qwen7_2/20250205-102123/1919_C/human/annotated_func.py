#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `n`, `a` will contain the first element of `lit` followed by any elements from `lit` that are greater than their preceding element, and `b` will contain all elements from `lit` that are less than or equal to their preceding element; `s` will be the total count of elements in `a` that are greater than their preceding element.
    #
    #This means that after processing all inputs, `a` will store the increasing subsequence found in `lit`, and `b` will store the non-increasing subsequence. The variable `s` will hold the total count of elements in `a` that form an increasing sequence with their preceding elements.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. It identifies the longest increasing subsequence in the list and counts the number of elements in this subsequence that are greater than their preceding element. The function prints this count for each test case.

