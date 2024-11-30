#State of the program right berfore the function call: n is a positive integer representing the number of employees, and the characters in the input string are either 'D' or 'R'.**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer representing the number of employees, characters in the input string are either 'D' or 'R', votes is assigned the input string after stripping any leading or trailing whitespaces and not empty. d_queue contains the indices of employees who voted 'D' in the order they appear in the string, r_queue contains the indices of employees who voted 'R' in the order they appear in the string.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: n is a positive integer, characters in the input string are either 'D' or 'R', votes is the input string after stripping any leading or trailing whitespaces and not empty. After all iterations of the loop, either d_queue or r_queue will be empty. If d_queue is empty, then all employees who voted 'D' have been paired with employees who voted 'R' based on their indices. If r_queue is empty, then all employees who voted 'R' have been paired with employees who voted 'D' based on their indices. The specific pairing order may vary depending on the values of d_index and r_index in each iteration of the loop.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is a positive integer. Characters in the input string are either 'D' or 'R'. Votes is the input string after stripping any leading or trailing whitespaces and not empty. After all iterations of the loop, either d_queue or r_queue will be empty. If d_queue is empty, then all employees who voted 'D' have been paired with employees who voted 'R' based on their indices. If r_queue is empty, then all employees who voted 'R' have been paired with employees who voted 'D' based on their indices. The specific pairing order may vary depending on the values of d_index and r_index in each iteration of the loop. After the execution of the if else block, either all employees who voted 'D' have been paired with employees who voted 'R' based on their indices (if d_queue was empty) or all employees who voted 'R' have been paired with employees who voted 'D' based on their indices (if r_queue was empty). The program prints 'D' if d_queue is not empty, otherwise it prints 'R'.
#Overall this is what the function does:The function reads an input string representing the political affiliation of employees, then pairs employees who voted 'D' and 'R' based on their indices. If there are more employees who voted 'D', it prints 'D'; otherwise, it prints 'R'.

