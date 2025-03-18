#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and n is the length of arr. The function is called once per test case, and there can be up to 2 * 10^4 test cases. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies `0 <= a_i < n`, and `n` is the length of `arr`. `nums` is a Counter object representing the counts of each element in `arr` with the counts of processed elements decremented accordingly. `start` is the first index that does not have any remaining elements to process. `vis` is a set containing all indices from 0 to `start - 1`.
    print(start)
    #This is printed: start (where start is the first index in arr that has not been processed)
#Overall this is what the function does:The function `func_1` processes a list of integers `arr` where each integer is within the range `[0, n-1]` and `n` is the length of `arr`. It prints the smallest integer that is missing from the sequence starting from `0` after accounting for the counts of each integer in the list. The function does not return any meaningful value; it either prints a number and exits or simply prints a number at the end of its execution.

