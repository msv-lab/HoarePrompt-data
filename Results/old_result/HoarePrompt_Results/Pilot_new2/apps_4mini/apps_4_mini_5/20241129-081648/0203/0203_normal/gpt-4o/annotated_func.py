#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200000, and the next line is a string of length n consisting of characters 'D' and 'R' representing the fractions of the employees.
def func():
    n = int(input())
    votes = input().strip()
    d_queue = []
    r_queue = []
    for (i, v) in enumerate(votes):
        if v == 'D':
            d_queue.append(i)
        else:
            r_queue.append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200000; `votes` is a string of length `n`; `d_queue` contains the indices of all 'D' characters in `votes`, and `r_queue` contains the indices of all 'R' characters in `votes`. If `votes` is empty, both `d_queue` and `r_queue` remain empty.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: `d_queue` and `r_queue` are both empty; if `d_queue` executed for at least one iteration, then there must have been at least one 'D' and at least one 'R' in the original `votes`; the loop had to run until either `d_queue` or `r_queue` was empty, meaning there could have been multiple pairs of indices processed based on their relative values, resulting in their respective indices being incremented by `n` and re-added to their queues.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`d_queue` and `r_queue` are both empty. If `d_queue` is not empty, then 'D' has been printed. If `d_queue` executed for at least one iteration, there must have been at least one 'D' and at least one 'R' in the original `votes`. If `d_queue` is empty and `r_queue` is also empty, then 'R' is printed.
#Overall this is what the function does:The function accepts an integer `n` followed by a string of length `n` consisting of characters 'D' and 'R'. It processes this string to simulate a voting mechanism where votes represented by 'D' and 'R' are compared based on their indices. The function determines the final winner after pairing votes: if there are remaining 'D' votes, it prints 'D'; if there are remaining 'R' votes, it prints 'R'. This function does not handle cases where `n` is less than 1 or where the input string may contain characters other than 'D' or 'R', and it assumes valid input as per the provided constraints.

