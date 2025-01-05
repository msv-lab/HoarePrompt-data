#State of the program right berfore the function call: **Precondition**: **t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 2*10^5, and s is a string of length n where each character is either 'R', 'S', or 'P'.**
def func():
    range = xrange
    input = raw_input
    mapper = {'R': 0, 'P': 1, 'S': 2}
    t = int(input())
    for _ in range(t):
        S = [mapper[c] for c in input()]
        
        count = [0] * 3
        
        for s in S:
            count[s] += 1
        
        maxi = max(range(3), key=count.__getitem__)
        
        maxi -= 2
        
        print('RPS'[maxi]) * len(S)
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop have finished, the values of the variables will be the same as in the initial state.
#Overall this is what the function does:The function `func` reads input values according to predefined constraints and relationships. It then processes the input characters 'R', 'P', 'S' into a count array and determines the maximum count character to output 'R', 'P', or 'S' accordingly. However, the actual logic of the code seems to have some issues, such as the incorrect calculation of the `maxi` value and the multiplication with `len(S)` when printing the output. These discrepancies should be addressed for the correct functionality of the function.

