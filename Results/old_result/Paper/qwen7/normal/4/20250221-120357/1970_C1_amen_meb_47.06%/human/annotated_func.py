#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: Output State: The loop will terminate when the input no longer consists of exactly two elements. After all iterations, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, `num1` and `num2` will hold the last pair of integers provided as input, and `numbers` is a list containing all pairs of integers `[num1, num2]` provided as input until the loop terminates.
    #
    #In simpler terms, after all iterations of the loop, `n` remains within its initial range, `t` stays as 1, `u` and `v` stay within their initial range, `num1` and `num2` will be the last two numbers entered, and `numbers` will contain every pair of numbers entered during the loop's execution.
    return numbers
    #The program returns a list named 'numbers' which contains every pair of integers [num1, num2] provided as input during the loop's execution, with each element in the list being a pair of integers where 1 ≤ u, v ≤ n, and n is an integer such that 2 ≤ n ≤ 2×10^5. The variables t, u, and v remain as 1, and the last pair of integers entered are stored in num1 and num2.
#Overall this is what the function does:The function processes pairs of integers [u, v] within the specified constraints (1 ≤ u, v ≤ n and 2 ≤ n ≤ 2×10^5), storing each valid pair in a list named 'numbers'. Upon completion, it returns the list 'numbers'. Throughout the process, the variable t remains as 1, and the last pair of integers entered are stored in num1 and num2.

