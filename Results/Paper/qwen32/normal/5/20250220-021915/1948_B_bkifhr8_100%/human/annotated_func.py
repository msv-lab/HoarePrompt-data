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
        
    #State: The output state after all iterations is a series of 'YES' or 'NO' printed for each of the `t` test cases, based on whether the condition was met for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it determines if the list can be modified by a specific rule (replacing a pair of adjacent numbers with a new number formed by concatenating the digits of the larger number followed by the smaller number, ensuring the resulting sequence is sorted) such that the final list is sorted in non-decreasing order. It prints 'YES' if the condition can be met for the test case, otherwise 'NO'.

