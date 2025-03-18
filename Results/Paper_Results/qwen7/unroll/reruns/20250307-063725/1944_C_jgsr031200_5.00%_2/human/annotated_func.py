#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\) (1 <= n <= 2 * 10^5).
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
        
    #State: The value of `start` is some integer `x`, `vis` contains all integers from 0 to `x`, and `nums` has been modified such that for each index `i` from 0 to `x`, `nums[i]` is less than or equal to 0, with at least one index `j` where `nums[j]` is exactly 0 or negative.
    print(start)
    #This is printed: start (where start is some integer x)
#Overall this is what the function does:The function accepts a list `arr` of non-negative integers and returns either a value or prints a value based on the elements in the list. Specifically, it iterates through the list, marking visited indices and decrementing their values. If it finds a sequence where the next index is valid and not visited, it continues; otherwise, it prints and returns the current index plus one. If it completes the loop without finding such a sequence, it prints and returns the current index.

