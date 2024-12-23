#State of the program right berfore the function call: ticket is a string consisting of exactly n digits (where 2 ≤ n ≤ 100 and each digit is between '0' and '9'), representing the golden ticket.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: `ticket` is a string consisting of exactly n digits (where 2 ≤ n ≤ 100 and each digit is between '0' and '9'), representing the golden ticket; `total_sum` is the sum of all digits in `ticket`; the total sum of the digits in `ticket` is even
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a non-empty string of exactly `n` digits (where 2 ≤ n ≤ 100 and each digit is between '0' and '9'), `total_sum` is the sum of all digits in `ticket`, `target_sum` is `total_sum // 2`, `curr_sum` is 0, and `segments` is the number of times `curr_sum` equals `target_sum`.
    return segments >= 2
    #The program returns True if there are at least 2 segments where curr_sum equals target_sum, otherwise False
#Overall this is what the function does:The function `func_1` accepts a string `ticket` consisting of exactly `n` digits (where `2 ≤ n ≤ 100` and each digit is between '0' and '9'). It calculates the sum of all digits in `ticket` and checks if this sum is even. If the sum is odd, it immediately returns `False`. Otherwise, it divides the sum by 2 to get `target_sum`. The function then iterates through each digit in `ticket`, accumulating a running sum (`curr_sum`). Whenever `curr_sum` equals `target_sum`, it increments the `segments` counter and resets `curr_sum`. After completing the iteration, the function returns `True` if `segments` is at least 2, indicating that there are at least two segments within `ticket` where the sum of digits equals `target_sum`. If no such segments exist, it returns `False`.

