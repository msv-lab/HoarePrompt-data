#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and n is the length of arr. The function is called multiple times for different test cases, where the total number of elements across all test cases does not exceed 2 * 10^5.
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
        
    #State: `vis` contains all processed integers, `start` is the integer just before the sequence breaks, `nums` has decremented counts for processed integers, and the function prints `start + 1`.
    print(start)
    #This is printed: start (where start is the integer just before the sequence breaks)
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` where each integer `a_i` satisfies `0 <= a_i < n` and `n` is the length of `arr`. It processes the list to find the smallest integer `start` such that the sequence starting from `0` cannot be continued by finding consecutive integers in the list. The function prints the integer just before the sequence breaks.

