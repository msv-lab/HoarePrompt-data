#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000, and the second line is a string of length n consisting of characters 'D' and 'R' representing the fractions of the employees.
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
        
    #State of the program after the  for loop has been executed: `d_queue` contains the indices of all 'D' characters in `votes`, `r_queue` contains the indices of all non-'D' characters in `votes`, and `n` is the total length of `votes`.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: `d_queue` is empty or `r_queue` is empty, `d_queue` may contain re-added indices from `d_queue` based on their relationships with indices from `r_queue`, while `r_queue` may contain re-added indices from `r_queue` based on their relationships with indices from `d_queue`. The final state of `d_index` and `r_index` will be the last values removed from their respective queues.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *If `d_queue` is not empty, the final state of `d_index` and `r_index` will be the last values removed from their respective queues, and the output will be 'D'. If `d_queue` is empty, then either `d_queue` or `r_queue` is empty, and the final state of `d_index` and `r_index` will be the last values removed from `r_queue`, as `d_queue` was not accessed. In both cases, `d_queue` and `r_queue` may contain re-added indices based on their relationships with each other.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 200,000) and a string of length `n` consisting of characters 'D' and 'R'. It simulates a process where indices of 'D' and 'R' characters compete against each other, with the character that appears first in the queue being re-added to the queue with an increment of `n` to its index. The function continues this process until one of the queues is empty and prints 'D' if characters 'D' remain or 'R' if characters 'R' remain.

