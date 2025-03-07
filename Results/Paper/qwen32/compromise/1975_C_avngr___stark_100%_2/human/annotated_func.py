#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: `t` is greater than or equal to the number of test cases executed, `n` is the integer input by the user for the current test case, `a` is a list of integers derived from the latest input for the current test case, and `max` is the maximum second smallest element found in any slice of length 3 from the list `a` for each test case. The loop has processed all test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and an array `a` of `n` integers. For each test case, it finds the maximum second smallest element in any contiguous subarray of length 3 from `a` and prints this value. If `n` is 2, it simply prints the minimum of the two elements.

