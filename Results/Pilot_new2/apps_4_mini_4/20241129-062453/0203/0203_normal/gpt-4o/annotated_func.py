#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000, and a string of length n consisting of characters 'D' and 'R' representing the fractions of the n employees where 'D' denotes depublicans and 'R' denotes remocrats.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `votes` is a string of length `n` consisting of 'D' and 'R'; `d_queue` is a list containing the indices of all 'D' characters in `votes`; `r_queue` is a list containing the indices of all 'R' characters in `votes`.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: `d_queue` is empty, `r_queue` is empty; if `votes` contained at least one 'D' and one 'R', then each 'D' and 'R' has competed against each other until they are exhausted, with the final `d_index` and `r_index` being the last indices that were compared before the queues were emptied. If `n` is the original number of votes, then all elements in `votes` have been processed.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`d_queue` and `r_queue` are empty. If `d_queue` is not empty, then it contains remaining 'D' votes, all elements in `votes` have been processed, and the output 'D' is printed. If `d_queue` is empty, both queues are empty, and all elements in `votes` have been processed, with `d_index` and `r_index` reflecting the last indices compared before the queues were emptied.
#Overall this is what the function does:The function accepts a positive integer `n` and a string `votes` of length `n` consisting of characters 'D' (depublicans) and 'R' (remocrats). It processes the votes in a competitive manner, simulating matchups between indices of 'D' and 'R'. If 'D' indices are exhausted before 'R', it prints 'R'; if 'R' indices are exhausted before 'D', it prints 'D'. The function does not handle cases where both 'D' and 'R' are absent, as it assumes the input will always contain at least one of each.

