#State of the program right berfore the function call: N is an integer such that 1 <= N <= 100, and S is a list of length N containing characters where each character is either 'P', 'W', 'G', or 'Y', with at least one 'P', one 'W', and one 'G' present in the list.
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: `N` is -1 if any character in `S` is 'Y', `S` is a list of characters from the original string input, and `i` is less than `N` or equal to the length of `S` - 1.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *`N` is -1, `S` is a list of characters derived from the original string input, and `i` is less than or equal to the length of `S` - 1. If `N` is -1, then 'Three' is printed.
#Overall this is what the function does:The function accepts an integer `N` (1 <= N <= 100) and a list `S` of length `N` containing characters 'P', 'W', 'G', or 'Y', ensuring at least one 'P', one 'W', and one 'G' are present in `S`. The function checks if any character in `S` is 'Y'; if so, it prints 'Four' and sets `N` to -1. If `N` is -1, it prints 'Three'. However, it does not return any values and does not handle cases where `N` is 0 or negative, nor does it account for the absence of 'P', 'W', or 'G'.

