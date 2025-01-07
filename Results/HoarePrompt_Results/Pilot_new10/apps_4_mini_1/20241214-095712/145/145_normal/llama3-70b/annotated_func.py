#State of the program right berfore the function call: ticket is a string of digits with a length between 2 and 100, where each digit is between 0 and 9.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False, indicating that the current value of `total_sum`, which is the sum of the digits in the `ticket` string, is odd.
    #State of the program after the if block has been executed: *`ticket` is a string of digits with a length between 2 and 100, where each digit is between 0 and 9; `total_sum` is the sum of the digits in `ticket`, and `total_sum` is an even number.
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string of digits with length between 2 and 100, `total_sum` is an even number formed by the sum of the digits in `ticket`, `target_sum` is `total_sum // 2`, `curr_sum` is the sum of the digits processed and may be less than `target_sum` if there are remaining digits not forming a complete segment, and `segments` is the total number of complete segments formed that equal `target_sum`.
    return segments >= 2
    #The program returns whether the number of complete segments formed that equal `target_sum` is greater than or equal to 2
#Overall this is what the function does:The function accepts a string `ticket` composed of digits with a length between 2 and 100. It returns False if the sum of the digits in `ticket` is odd; otherwise, it returns True if at least two complete segments can be formed, each equal to half of the total sum of digits. If less than two segments can be formed, it returns False.

