#State of the program right berfore the function call: N is an integer such that 1 <= N <= 20, and H is a list of N integers where each integer H_i satisfies 1 <= H_i <= 100.
def func():
    n = int(raw_input().strip())
    inp = map(int, raw_input().strip().split(' '))
    max = 0
    ans = 0
    for h in inp:
        if max <= h:
            max = h
            ans += 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= N <= 20, `H` is a list of N integers where each integer `H_i` satisfies 1 <= `H_i` <= 100, `n` is an input integer such that 1 <= n <= 20, `inp` is a map object containing integers read from the input and must contain at least `n` items. `max` is the maximum value among the integers in `inp`, and `ans` is the number of times `max` was updated during the loop (i.e., the number of integers in `inp` that were greater than or equal to the previous `max`). If `inp` is empty, `max` remains 0 and `ans` remains 0.
    print(ans)
#Overall this is what the function does:The function reads two lines of input: the first line is an integer `N` (1 <= N <= 20), and the second line is a space-separated list of `N` integers (1 <= H_i <= 100). It then calculates the number of integers in the list that are greater than or equal to the current maximum value encountered so far, starting from the beginning of the list. The function prints this count and does not return any value. If the input list is empty, the function prints 0.

