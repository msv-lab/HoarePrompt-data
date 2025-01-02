#State of the program right berfore the function call: The input consists of two integers n and k, where 2 ≤ n ≤ 100 and 1 ≤ k ≤ n - 1, representing the number of cells in the line and the length of one grasshopper's jump respectively. The second line is a string of length n containing characters '.', '#', 'G', and 'T', where '.' denotes an empty cell, '#' denotes a cell with an obstacle, 'G' denotes the grasshopper's starting position, and 'T' denotes the insect's position. It is guaranteed that both 'G' and 'T' appear exactly once in the string.
def func():
    l1 = list(map(int, raw_input().split()))
    n, k = l1[0], l1[1]
    l = raw_input()
    mestot = None
    mestok = None
    for i in range(len(l)):
        if l[i] == 'G':
            mestok = i
        
        if l[i] == 'T':
            mestot = i
        
        if mestok != None and mestot != None:
            break
        
    #State of the program after the  for loop has been executed: `l1` is ['n', 'k'], `l` is a non-empty string, `mestok` is the index of the last 'G' in `l` (or None if 'G' is not found), `mestot` is the index of the last 'T' in `l` (or the index of the last 'G' if 'T' is not found or None if neither 'G' nor 'T' is found).
    fl = True
    if (abs(mestot - mestok) % k == 0) :
        for i in range(mestok, len(l), k):
            if l[i] == '#':
                fl = False
                break
            
        #State of the program after the  for loop has been executed: Output State:
        if (fl != False and mestot < mestok) :
            l = l[::-1]
            for i in range(len(l)):
                if l[i] == 'G':
                    mestok = i
                
                if l[i] == 'T':
                    mestot = i
                
            #State of the program after the  for loop has been executed: `fl` is not `False`, `mestot` is the index of the last 'T' in the list `l` or the original value of `mestot` if there is no 'T', `mestok` is the index of the first 'G' in the list `l` or the original value of `mestok` if there is no 'G', `l` is the reversed version of its original state, and `i` is the length of the list `l`.
            for i in range(mestok, len(l), k):
                if l[i] == '#':
                    fl = False
                    break
                
            #State of the program after the  for loop has been executed: 
        #State of the program after the if block has been executed: *fl is not False and mestot is less than mestok. If this condition is true, no specific changes are made to the output state. Since there is no else part, the output state remains unchanged.
        if (fl == True) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`fl` is not False, `mestot` is less than `mestok`. If `fl` is True, the output is 'YES'. Otherwise, the output remains unchanged.
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`fl` is True, `mestot` is less than `mestok`. If `abs(mestot - mestok) % k == 0`, the output is 'YES'. Otherwise, the program checks if `abs(mestot - mestok) % k != 0` and does not change the output.
#Overall this is what the function does:The function accepts two integers \( n \) and \( k \), and a string representing \( n \) cells. It determines whether a grasshopper, starting at the 'G' position, can jump to the 'T' position using jumps of length \( k \), without landing on any obstacles ('#'). If the grasshopper can reach the 'T' position under these conditions, the function prints 'YES'; otherwise, it prints 'NO'. The function handles edge cases such as when 'G' or 'T' are not found in the string, and when the 'T' is not reachable due to obstacles or distance constraints.

