#State of the program right berfore the function call: N is an integer such that 1 <= N <= 100, and S is a list of strings where each string is one of 'P', 'W', 'G', or 'Y', and the list contains at least one 'P', one 'W', and one 'G'.
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: `N` is -1 if at least one 'Y' is in `S`, otherwise `N` is equal to the initial input value.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *If `N` is -1, indicating that at least one 'Y' is in `S`, then 'Three' is printed. Otherwise, `N` retains its initial input value.
#Overall this is what the function does:The function accepts an integer N (1 <= N <= 100) and a list of strings S (containing at least one 'P', one 'W', and one 'G'). It checks if there is at least one 'Y' in the list S. If 'Y' is present, it prints 'Four' and subsequently prints 'Three'. If 'Y' is not present, it does nothing further. The function does not return any values.

