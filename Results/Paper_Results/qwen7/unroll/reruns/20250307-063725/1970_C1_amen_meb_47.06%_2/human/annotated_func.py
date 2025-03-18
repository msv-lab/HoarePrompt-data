#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element. The tree represented by the edges has exactly two leaves.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: The variable `numbers` will contain a list of edge pairs (as lists of two integers each) entered by the user until a line with less than two elements is entered.
    return numbers
    #The program returns a list of edge pairs (each pair is a list of two integers) entered by the user until a line with less than two elements is entered.
#Overall this is what the function does:The function reads edge pairs (each pair consisting of two integers) from user input until a line with less than two elements is entered. It then returns a list of these edge pairs.

