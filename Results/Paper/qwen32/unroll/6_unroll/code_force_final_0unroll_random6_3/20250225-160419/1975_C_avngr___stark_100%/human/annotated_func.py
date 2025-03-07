#State of the program right berfore the function call: Each test case contains an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The printed results for each of the t test cases, where each result is either the minimum of two integers if n is 2, or the maximum median of the medians of all subarrays of length 3 if n is greater than 2.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, if `n` is 2, it outputs the minimum of the two integers. If `n` is greater than 2, it finds and outputs the maximum median value among all subarrays of length 3 within the list.

