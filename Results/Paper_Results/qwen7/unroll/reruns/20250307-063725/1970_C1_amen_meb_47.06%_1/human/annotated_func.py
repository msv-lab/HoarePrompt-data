#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains t integers such that 1 ≤ u_1, ..., u_t ≤ n.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: Output State: The `numbers` list will contain all pairs of integers (num1, num2) entered by the user until a line with less than 2 elements is entered.
    #
    #Explanation: The loop continues to run indefinitely (`while True`) until it encounters a line of input that does not consist of exactly two space-separated integers. Each valid line of input is split into two integers, which are then appended as a list `[num1, num2]` to the `numbers` list. Therefore, the final state of `numbers` will be a list of all such pairs entered by the user before an invalid input is provided.
    return numbers
    #The program returns a list of all pairs of integers (num1, num2) entered by the user until a line with less than 2 elements is entered.
#Overall this is what the function does:The function accepts no parameters and returns a list of all pairs of integers (num1, num2) entered by the user until a line with less than 2 elements is entered. The function reads input from the user repeatedly, splits each line into two integers, and appends them as a list `[num1, num2]` to the `numbers` list. The process continues until a line of input does not consist of exactly two space-separated integers, at which point the function returns the accumulated list of pairs.

