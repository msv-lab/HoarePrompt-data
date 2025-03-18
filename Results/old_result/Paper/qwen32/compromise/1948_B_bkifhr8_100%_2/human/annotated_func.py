#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3. For each test case, n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 99.
def func():
    n = int(input())
    for _ in range(n):
        m = int(input())
        
        arr = [int(i) for i in input().split()]
        
        ans = True
        
        for i in range(m - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                nums = [int(i) for i in str(arr[i - 1])] + [arr[i]]
                if nums != sorted(nums):
                    ans = False
                    break
                arr[i - 1] = nums[0]
        
        print(['NO', 'YES'][ans])
        
    #State: The loop has completed all `t` iterations, and the program has printed 'YES' or 'NO' for each set of input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it determines if the list can be transformed into a non-decreasing sequence by repeatedly replacing a pair of adjacent elements where the first is greater than the second, with a new element formed by concatenating the digits of the first element and the second element, followed by sorting the resulting digits. It prints 'YES' if such a transformation is possible for the list, otherwise it prints 'NO'.

