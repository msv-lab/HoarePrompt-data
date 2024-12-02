#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000, and there is a string of length n consisting of characters 'D' (for depublicans) and 'R' (for remocrats).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200000, `votes` is a non-empty string, `d_queue` contains the indices of all 'D' characters in `votes`, `r_queue` contains the indices of all characters in `votes` that are not 'D'.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: `d_queue` and `r_queue` may be empty depending on the comparisons of indices; the final state of `d_queue` will include elements of the form `d_index + kn` for some integer `k` if those indices were initially less than the corresponding elements in `r_queue`; the final state of `r_queue` will include elements of the form `r_index + kn` for some integer `k` if those indices were initially greater than or equal to the corresponding elements in `d_queue`. If both queues are empty, all indices have been processed through the loop.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *If `d_queue` is not empty, then elements from `d_queue` have been processed and 'D' has been printed to the output. If `d_queue` is empty, then 'R' has been printed, and the state of `r_queue` will depend on the comparisons of indices; both queues may be empty if all indices have been processed.
#Overall this is what the function does:The function accepts a positive integer `n` and a string of length `n` consisting of characters 'D' and 'R'. It then processes the indices of 'D' and 'R' characters in a queue-like fashion, comparing their indices to determine which character ultimately "wins." The function will print 'D' if 'D' characters remain after processing, or 'R' if 'R' characters remain. If both queues are empty, the last printed character is the winner based on the comparisons that were made. The function assumes input string consists only of 'D' and 'R' characters without handling invalid inputs.

