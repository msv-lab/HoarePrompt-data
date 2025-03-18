#State of the program right berfore the function call: arr is a list of non-negative integers where each integer is less than the length of the list, and the length of arr is between 1 and 2 * 10^5.
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
        
    #State: The loop will print the smallest integer `x` such that `x` is not present in `arr` and then return. The `vis` set will contain all integers from 0 up to `x-1` that were present in `arr`. The `nums` Counter will be updated to reflect the decremented counts of these integers, and the count of `x-1` will be 0. The `start` variable will be equal to `x-1` when the loop exits.
    print(start)
    #This is printed: start (where start is the largest integer in `arr` that is present, or the largest integer less than the smallest integer not present in `arr`)
#Overall this is what the function does:The function `func_1` accepts a list `arr` of non-negative integers, where each integer is less than the length of the list, and the length of `arr` is between 1 and 2 * 10^5. It prints the smallest integer `x` such that `x` is not present in `arr`. The function does not return any value. After the function concludes, the `vis` set will contain all integers from 0 up to `x-1` that were present in `arr`, and the `nums` Counter will be updated to reflect the decremented counts of these integers, with the count of `x-1` being 0. The `start` variable will be equal to `x-1` when the loop exits.

