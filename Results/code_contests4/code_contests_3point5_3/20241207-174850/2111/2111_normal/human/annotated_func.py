#State of the program right berfore the function call: **
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: If there is an element 'Y' in the list `S`, then `N` will be -1 and the loop will break. Otherwise, `N` will be greater than 0, and `S` will remain a non-empty list of strings obtained by splitting the input.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *If there is an element 'Y' in the list `S`, then `N` will be -1 and the loop will break, and the program will print 'Three'. Otherwise, if `N` is greater than 0 and `S` remains a non-empty list of strings obtained by splitting the input.
#Overall this is what the function does:The function `func` reads an input `N`, then reads a list of strings `S` from the input. It iterates over the elements of `S` and if it finds an element 'Y', it prints 'Four', sets `N` to -1, and breaks the loop. After the loop, if `N` is -1, it prints 'Three'. If there is no 'Y' in `S`, the program does not print anything. The function does not have any specific return value.

