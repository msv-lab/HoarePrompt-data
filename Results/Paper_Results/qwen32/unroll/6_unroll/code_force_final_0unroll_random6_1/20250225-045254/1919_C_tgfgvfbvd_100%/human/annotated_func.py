#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5), representing the size of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), representing the elements of the array a. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: the variables `a`, `b`, and `c` are reset to `float('inf')`, `float('inf')`, and `0` respectively for each test case, and no other variables in the precondition are affected by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and an array `a` of `n` integers. For each test case, it calculates and prints the number of times the smallest and second smallest elements in the array are replaced during a specific traversal of the array.

