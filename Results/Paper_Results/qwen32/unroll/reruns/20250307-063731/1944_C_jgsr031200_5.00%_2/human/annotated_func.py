#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and n is the length of the list arr. The function is called multiple times for different test cases, with the total sum of n across all test cases not exceeding 2 * 10^5.
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
        
    #State: The loop prints the first integer `start + 1` for which `nums[start + 1]` is 0. The `vis` set contains all processed `start` values, and the `nums` counter has decremented the counts of these values. The `start` variable holds the last processed value.
    print(start)
    #This is printed: start (where start is the last processed value such that nums[start + 1] is 0)
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input, where each integer is between 0 and the length of the list minus one. It processes the list and prints the smallest integer `x` such that `x` or `x-1` does not appear in the list, or the largest integer processed if all integers up to that point are present. The function modifies the list indirectly through a counter and a set but does not return a value; instead, it outputs the result directly.

