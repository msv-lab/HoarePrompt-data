#State of the program right berfore the function call: n is an integer such that 1 <= n <= 200,000. The characters in the input are either 'D' or 'R'.**
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
        
    #State of the program after the  for loop has been executed: n is an input integer between 1 and 200,000; votes is a string with at least one character; i is equal to the total number of characters in the votes string minus 1. If v is 'D', d_queue is a list containing the indices of all 'D' characters in the votes string. If v is not 'D', r_queue is a list containing the indices of all non-'D' characters in the votes string.
    while d_queue and r_queue:
        d_index = d_queue.pop(0)
        
        r_index = r_queue.pop(0)
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
        
    #State of the program after the loop has been executed: After all iterations of the loop have executed, `n` is the original input integer, `votes` is the string with at least one character, `i` is equal to the total number of characters in the votes string minus 1. If `v` is 'D', `d_queue` is empty. If `v` is not 'D', `r_queue` is empty.
    if d_queue :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *After the execution of the if else block, `n` is the original input integer, `votes` is the string with at least one character, `i` is equal to the total number of characters in the votes string minus 1. If `v` is 'D', `d_queue` is empty. If `v` is not 'D', `r_queue` is empty. If `d_queue` is true, it is empty and the string 'D' is printed. If `d_queue` is false, after printing 'R', `n` is the original input integer, `votes` is the string with at least one character, `i` is equal to the total number of characters in the votes string minus 1, `v` is not 'D', `r_queue` is empty, and `d_queue` is empty.
#Overall this is what the function does:The function `func` does not accept any parameters. It processes a sequence of characters representing Democrats ('D') and Republicans ('R') in a queue. The function then simulates the process of removing individuals from the queue based on their party affiliation:
1. If the first person in the queue is a Democrat ('D'), they are removed.
2. If the first person is a Republican ('R'), they are removed, and the person behind them moves to the end of the queue.
This removal process continues cyclically until the queue is empty. The function finally prints the party affiliation of the last person remaining in the queue, which could be 'D' or 'R'.

