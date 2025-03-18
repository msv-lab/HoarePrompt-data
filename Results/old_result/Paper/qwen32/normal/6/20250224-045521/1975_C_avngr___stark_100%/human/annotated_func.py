#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The number of test cases t (1 ≤ t ≤ 500) is provided first, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: t is an input integer representing the number of test cases (0 ≤ t ≤ 500); n is an input integer and can be any value from 2 to 500; a is a list of integers obtained from the input for each test case; max is the maximum value of the middle elements of all possible 3-element sorted slices of the list a for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it finds the maximum value of the middle element in all possible 3-element sorted subarrays of the list and prints this value. If `n` is 2, it simply prints the minimum of the two elements.

