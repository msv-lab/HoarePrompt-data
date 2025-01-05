#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 100, and S is a list of N characters where each character is one of 'P', 'W', 'G', or 'Y'. There are at least one 'P', one 'W', and one 'G' in the list.
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 100; `S` is a list of `N` characters; if any character in `S` is 'Y', then 'Four' has been printed and the loop has exited early; otherwise, the loop has completed without printing anything.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 <= `N` <= 100. If `N` is equal to -1, 'Three' has been printed. Otherwise, if any character in `S` is 'Y', then 'Four' has been printed and the loop has exited early; otherwise, the loop has completed without printing anything.
#Overall this is what the function does:The function reads an integer `N` and a list `S` of `N` characters. If any character in `S` is 'Y', it prints 'Four' and sets `N` to -1. If 'Y' was found, it subsequently prints 'Three'. If 'Y' is not found, the function does not print anything. The function assumes that `S` contains at least one 'P', one 'W', and one 'G', but it does not check for them explicitly. Thus, it may not handle cases where `S` does not meet this condition, leading to potential unexpected behavior.

