#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array. The number of test cases t satisfies 1 ≤ t ≤ 500, and the sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: For each test case, the maximum value of the minimum of consecutive elements in the list `a` is printed. The variables `t`, `n`, and `a` will hold the values from the last test case processed. The variable `max` will hold the result of the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it finds and prints the maximum value of the minimum of consecutive elements in the list.

