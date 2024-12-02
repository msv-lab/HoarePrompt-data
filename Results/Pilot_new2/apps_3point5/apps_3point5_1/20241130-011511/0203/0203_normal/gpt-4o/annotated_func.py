#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000. The input characters are either 'D' or 'R'.**
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 200,000; `votes` contains the input string stripped of any leading or trailing whitespace; `d_queue` contains the indices of all 'D' elements in the `votes` list in the order they appeared; `r_queue` contains the indices of all 'R' elements in the `votes` list in the order they appeared.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: After the loop executes, `n` remains the same as the original input integer between 1 and 200,000. `votes` still contains the input string stripped of any leading or trailing whitespace. `d_queue` is empty as all elements have been removed, and `r_queue` contains the elements that were not processed. The final values of `d_index` and `r_index` depend on the operations performed during the loop iterations, where `d_index` and `r_index` are the last values assigned to them during the loop execution.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *After the if-else block executes, `n` remains the same as the original input integer between 1 and 200,000. `votes` still contains the input string stripped of any leading or trailing whitespace. `d_queue` is empty. `r_queue` contains the elements that were not processed. The final values of `d_index` and `r_index` depend on the operations performed during the loop iterations, where `d_index` and `r_index` are the last values assigned to them during the loop execution. If `d_queue` is empty, the program prints 'R'.
#Overall this is what the function does:The function `func` reads an integer `n` (1 ≤ n ≤ 200,000) and a string of characters 'D' or 'R'. It categorizes the indices of 'D' and 'R' characters into separate queues, then processes these queues based on their indices. It iterates over the queues, moving indices by `n` positions if the 'D' index is smaller than the 'R' index. Finally, it prints 'D' if the 'D' queue is not empty, otherwise 'R'.

