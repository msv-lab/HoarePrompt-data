#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and the length of arr is n, with 1 <= n <= 2 * 10^5. The function will be called multiple times with different arrays, and the sum of all n values across the test cases does not exceed 2 * 10^5.
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
        
    #State: The loop will print and return `start + 1`, where `start` is the last consecutive integer found in the list `arr` starting from 0.
    print(start)
    #This is printed: start (where start is the last consecutive integer found in the list `arr` starting from 0)
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer `a_i` satisfies `0 <= a_i < n` and the length of `arr` is `n`. It prints and returns the smallest integer `k` such that the sequence of integers from `0` to `k-1` can be formed using the elements in `arr`. If the sequence can be formed up to `start`, it prints and returns `start + 1`; otherwise, it prints and returns `start`.

