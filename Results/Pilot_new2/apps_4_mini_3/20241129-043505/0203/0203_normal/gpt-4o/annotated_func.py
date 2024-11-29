#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000, and a string of length n consisting of characters 'D' and 'R', where 'D' represents a depublican and 'R' represents a remocrat.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 200,000; `d_queue` contains the indices of all 'D' votes, and `r_queue` contains the indices of all 'R' votes; the length of `votes` is equal to `n`.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: `d_queue` and `r_queue` contain indices that could not be matched, with `d_queue` and `r_queue` potentially containing indices that are greater than their original values by multiples of `n`, indicating the number of cycles processed. One of the queues is empty, while the other may contain indices that are greater than or equal to the initial indices.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`d_queue` and `r_queue` contain indices that could not be matched. If `d_queue` is not empty, 'D' has been printed. If `d_queue` is empty and `r_queue` contains indices, which are greater than or equal to the initial indices, then 'R' has been printed.
#Overall this is what the function does:The function accepts an integer `n` and a string of length `n` consisting of 'D' and 'R' characters, simulates a cyclic matchup between the votes, and prints 'D' if depublicans win or 'R' if remocrats win based on the remaining unmatched votes.

