#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3. Each test case consists of two lines: the first line contains a single integer n such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n such that 0 <= a_i <= 99.
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
        
    #State: Output State: t is a positive integer such that 1 <= t <= 10^3, n is an input integer such that 2 <= n <= 50, each iteration of the loop processes a new input integer m and a list of integers arr, and prints either 'NO' or 'YES' based on whether the list arr satisfies the given condition after processing.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) (2 ≤ \( n \) ≤ 50) followed by \( n \) integers \( a_1, a_2, \ldots, a_n \) (0 ≤ \( a_i \) ≤ 99). For each test case, it checks if rearranging any adjacent pair of elements can make the sequence non-decreasing. If such a rearrangement is possible, it prints 'YES'; otherwise, it prints 'NO'. The function implicitly uses the value of \( t \) (1 ≤ \( t \) ≤ 10^3) from the input structure but does not return it.

