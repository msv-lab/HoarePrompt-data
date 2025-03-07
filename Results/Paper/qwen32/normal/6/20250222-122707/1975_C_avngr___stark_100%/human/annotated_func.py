#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The number of test cases t (1 ≤ t ≤ 500) is provided at the beginning, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: `t` is 0, indicating all test cases have been processed; `n` is the integer value from the last test case and is at least 3; `a` is the list of `n` integers from the last test case; `max` is the maximum value of the middle elements of all possible slices of 3 consecutive elements in the last array `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it finds and prints the maximum value of the middle elements in all possible slices of 3 consecutive elements in the array `a`. If `n` is 2, it simply prints the minimum value of the two elements.

