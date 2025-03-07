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
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies `0 <= a_i < n`, and `n` is the length of `arr`; `nums` is a Counter object representing the frequency of each element in `arr` with the counts of elements from 0 to `start` appropriately decreased; `start` is the last value that had a non-zero count in `nums`; `vis` is a set containing the values from 0 to `start - 1`. The function prints `start + 1` and terminates.
    #
    #Output State:
    print(start)
    #This is printed: start (where start is the last value that had a non-zero count in nums)
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input, where each integer `a_i` satisfies `0 <= a_i < n` and `n` is the length of `arr`. It processes the list to find a specific integer value and prints that value. The function does not return any value (returns `None`).

