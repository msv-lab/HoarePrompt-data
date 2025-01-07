#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000. Each character in the input string represents an employee from either 'D' (depublicans) or 'R' (remocrats).**
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
        
    #State of the program after the  for loop has been executed: n is an input integer such that 1 ≤ n ≤ 200,000, votes is a non-empty string. After the loop executes, d_queue contains the indices of all 'D' characters in the order they appeared in the input string, r_queue contains the indices of all 'R' characters in the order they appeared in the input string.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: n is an input integer such that 1 ≤ n ≤ 200,000, votes is a non-empty string. After the loop executes, d_queue and r_queue are empty. The loop will execute as long as both d_queue and r_queue are not empty. After the loop finishes, d_index and r_index will contain the indices of 'D' and 'R' characters respectively in the order they appeared in the input string. If d_index is less than r_index, a new element will be added to d_queue which is equal to the previous d_index plus n. If d_index is greater than or equal to r_index, r_queue will have r_index + n appended to it.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is an input integer such that 1 ≤ n ≤ 200,000, votes is a non-empty string. After the loop executes, d_queue and r_queue are empty. The loop will execute as long as both d_queue and r_queue are not empty. After the loop finishes, d_index and r_index will contain the indices of 'D' and 'R' characters respectively in the order they appeared in the input string. If d_index is less than r_index, a new element will be added to d_queue which is equal to the previous d_index plus n. If d_index is greater than or equal to r_index, r_queue will have r_index + n appended to it. If d_queue is not empty, the code snippet prints 'D' but does not affect any other variables. If d_queue is empty, the program will not enter the loop and the output state remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `votes` representing employees from either 'D' (depublicans) or 'R' (remocrats). It then assigns the indices of 'D' and 'R' characters to separate queues based on their appearance order. The function simulates a process where 'D' and 'R' employees are removed from their respective queues at the same time and added back with an offset of `n`. After this simulation, if the 'D' queue is not empty, it prints 'D'; otherwise, it prints 'R'.

