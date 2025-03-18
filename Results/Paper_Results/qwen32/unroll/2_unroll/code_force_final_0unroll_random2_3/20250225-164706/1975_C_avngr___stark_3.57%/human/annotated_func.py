#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The total number of elements across all test cases does not exceed 10^5.
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
        
    #State: For each test case, the maximum value of the minimum of consecutive elements in the array `a` is printed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the maximum value of the minimum of consecutive elements in the array.

