#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 99.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^3; `n` is the integer input by the user, where 2 ≤ n ≤ 50; `a` is a list of `n` integers where each integer `a_i` satisfies 0 ≤ `a_i` ≤ 99; the loop has executed `n` times, with `m` being an input integer and `arr` being a list of integers provided by the user input, potentially modified if `arr[i] < arr[i - 1]` and `nums` is sorted; `ans` is True if all `nums` formed during the loop iterations were sorted, otherwise `ans` is False for each iteration, and the program has printed 'YES' or 'NO' for each iteration based on the value of `ans`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks a list of integers to determine if a specific condition is met: when any integer in the list is less than the preceding integer, the digits of the preceding integer along with the current integer should form a sorted sequence. If this condition holds for all such pairs in the list, it prints "YES"; otherwise, it prints "NO".

