#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, representing the size of the array a, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all the iterations, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer greater than 0, `lit` is a list of integers derived from the input, `a` is a list containing the first element of `lit` and all elements from `lit` that are not greater than any preceding element in `lit`, `b` is a list containing all elements in `lit` that are greater than the last element in `a` at the time they were encountered, `cp` is 0, `i` is `len(a) + len(b) - 2` for the last iteration, and `s` is the total number of times an element in `a` was greater than its preceding element plus the total number of times an element in `b` (excluding the first element) was greater than its preceding element across all test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of an integer `n` followed by a list of `n` integers. The function processes each test case by splitting the list into two sublists: `a` contains the first element and all subsequent elements that are not greater than the last element in `a`, while `b` contains all elements that are greater than the last element in `a`. The function then calculates the total number of increasing pairs within both `a` and `b` and prints this count for each test case. After processing all test cases, the function completes without returning any value.

