#State of the program right berfore the function call: n is a positive integer, employees belong to either 'D' (depublicans) or 'R' (remocrats).**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `employees` belong to either 'D' or 'R', `votes` is a string with at least 1 character. If all the characters in `votes` are 'D', `d_queue` contains the indices of all 'D' characters in order, `r_queue` is an empty list. If all the characters in `votes` are 'R', `r_queue` contains the indices of all 'R' characters in order, `d_queue` is an empty list. If there are both 'D' and 'R' characters in `votes`, `d_queue` contains the indices of 'D' characters in order, `r_queue` contains the indices of 'R' characters in order.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: After all iterations of the loop, either `d_queue` or `r_queue` will be empty depending on the initial configuration of `votes`. The `d_queue` will contain the indices of 'D' characters that were processed, and the `r_queue` will contain the indices of 'R' characters that were processed. The values of `d_index` and `r_index` will be the last popped values from the respective queues.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *After the if else block executes, either `d_queue` or `r_queue` will be empty based on the initial configuration of `votes`. If `d_queue` is not empty, then it will contain the indices of 'D' characters that were processed, `r_queue` will contain the indices of 'R' characters that were processed, `d_index` and `r_index` will be the last popped values from the respective queues, and the function will process the elements in `d_queue`. If the else part is executed, `d_queue` will be empty, `r_queue` will contain the indices of 'R' characters that were processed, `d_queue` will contain the indices of 'D' characters that were processed, `d_index` and `r_index` will be the last popped values from the respective queues, and 'R' is processed.
#Overall this is what the function does:The function reads an integer n and a string of votes containing 'D' and 'R' characters. It then processes the votes based on the indices of 'D' and 'R' characters in the input string. The function simulates a voting process where 'D' and 'R' employees are represented by queues. It iterates through the queues, updating indices based on the value of n. At the end, it determines the majority party by checking which queue is empty. If there is a tie, it returns "Tie".

