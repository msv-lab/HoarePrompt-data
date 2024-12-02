#State of the program right berfore the function call: nums is a list of integers.**
def func_1(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                count += 1
        
    #State of the program after the  for loop has been executed: Output State: `nums` is a list of integers, `count` is the number of times the XOR operation between any pair of elements in `nums` results in an even number, `i` is equal to `len(nums) - 1`, `j` is equal to `len(nums)`, the loop has finished executing. If `nums` has fewer than 2 elements, `count` remains 0.
    return count
    #The program returns the number of times the XOR operation between any pair of elements in `nums` results in an even number
#Overall this is what the function does:The function accepts a list of integers `nums` and calculates the number of times the XOR operation between any pair of elements in `nums` results in an even number. If `nums` has fewer than 2 elements, the function returns 0.

