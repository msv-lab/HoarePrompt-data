#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\) (i.e., 1 ≤ n ≤ 2⋅10^5).
def func_1(arr):
    nums = c.Counter(arr)
    start = 0
    vis = set()
    while nums.get(start, 0):
        vis.add(start)
        
        nums[start] -= 1
        
        if nums.get(start + 1, 0):
            nums[start + 1] -= 1
            start += 1
        else:
            print(start + 1)
            return
        
    #State: Output State: `start` is the last index where `nums[start]` is greater than 0; `nums[0]` is `nums[0] - (start)`, `nums[1]` is `nums[1] - (start-1)`, ..., `nums[start-1]` is `nums[start-1] - 1`, `vis` contains the elements from 0 to `start-1`.
    #
    #Explanation: The loop continues as long as there are non-zero values in `nums` starting from `start`. After each iteration, `start` is incremented, and the corresponding value in `nums` is decremented. If `nums[start + 1]` is not truthy, the loop prints `start + 1` and returns, stopping further iterations. Therefore, the final state will have `start` at the last position where `nums[start]` is still greater than 0. All previous positions from `start` back to 0 will have their values in `nums` decremented accordingly, and all indices from 0 to `start-1` will be in the `vis` set.
    print(start)
    #This is printed: start + 1 (where start is the last index where nums[start] is greater than 0)
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\) (i.e., 1 ≤ n ≤ 2⋅10^5). It processes the list by counting the occurrences of each integer using a counter. Then, it iterates through the list, decrementing counts and tracking visited indices until it finds the last index where the count is still greater than zero. Finally, it prints this last index and ends without returning any value.

