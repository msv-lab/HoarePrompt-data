#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500), the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 10^5), the length of the array a. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9), the elements of the array a. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: After executing all iterations, the variable `t` remains unchanged. For each test case, the maximum value of the minimum of consecutive elements in the array `a` is printed. The variables `n`, `a`, and `max` are not retained after their respective test case is processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers. For each test case, it finds and prints the maximum value of the minimum of consecutive elements in the array.

