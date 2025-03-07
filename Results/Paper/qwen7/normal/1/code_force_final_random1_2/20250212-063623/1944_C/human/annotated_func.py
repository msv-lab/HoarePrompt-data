#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\) (i.e., 1 ≤ n ≤ 2 \cdot 10^5).
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
        
    #State: Output State: `start` is 4, `vis` is a set containing 0, 1, 2, 3, and 4, and `nums[4]` is either 0 or None (since it was decremented by 1 during the last iteration and the loop condition no longer holds).
    #
    #Explanation: After the loop has executed all its iterations, `start` would be incremented to 4 because the loop continues as long as `nums.get(start, 0)` is truthy. Since we know from the given conditions that the loop runs exactly 4 times, `start` will be 4 at the end. The set `vis` contains all indices from 0 to 3 because each index was visited exactly once. Finally, `nums[4]` is either 0 or None because it was decremented by 1 during the last iteration, and the loop condition `nums.get(start, 0)` becomes false, causing the loop to terminate.
    print(start)
    #This is printed: 4
#Overall this is what the function does:The function accepts a list `arr` of non-negative integers and performs operations to find and print the smallest index `start` such that `start + 1` is not present in the list. It prints the value of `start` which will be 4 in this case. The function does not return any value.

