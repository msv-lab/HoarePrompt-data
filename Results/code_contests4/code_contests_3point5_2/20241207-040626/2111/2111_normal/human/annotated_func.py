#State of the program right berfore the function call: N is an integer such that 1 <= N <= 100, and S_i represents the color of the i-th arare and can be one of the following values: `P`, `W`, `G`, `Y`.
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: If there is an element 'Y' in the list `S`, then `N` will be -1. Otherwise, `N` will retain its original input value.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *If there is an element 'Y' in the list `S`, then `N` will be -1 and 'Three' is printed. Otherwise, `N` will retain its original input value.
#Overall this is what the function does:The function `func` reads an integer `N` and a list of strings `S` representing the colors of different arare. If the list `S` contains the color 'Y', the function prints 'Four' and sets `N` to -1. Subsequently, if `N` is -1, it prints 'Three'. The function does not explicitly return any value.

