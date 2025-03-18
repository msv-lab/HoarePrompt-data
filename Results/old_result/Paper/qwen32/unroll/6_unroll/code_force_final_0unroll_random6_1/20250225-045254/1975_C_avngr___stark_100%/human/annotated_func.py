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
        
    #State: For each test case, the output will be the maximum median value of all contiguous subarrays of length 3 in the array `a`. If the array length `n` is 2, it will output the minimum value of the two elements.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and an array `a` of `n` integers. For each test case, if `n` is 2, it outputs the minimum of the two integers. Otherwise, it finds and outputs the maximum median value of all contiguous subarrays of length 3 in the array `a`.

