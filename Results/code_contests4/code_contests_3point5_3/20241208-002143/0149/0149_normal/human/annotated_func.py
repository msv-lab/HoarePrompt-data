#State of the program right berfore the function call: n is an even integer greater than or equal to 2.**
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: `n` is an even integer greater than or equal to 2, `p` is a list of integers where each element is one less than the original input values, `even` is the sum of absolute differences between `i * 2` and `p[i]` for all iterations of the loop, `odd` is the sum of absolute differences between `i * 2 + 1` and `p[i]` for all iterations of the loop.
    print(min(even, odd))
#Overall this is what the function does:The function `func` reads input from the user, processes it based on the constraints of `n` being an even integer greater than or equal to 2 and updates the values of `p`, `even`, and `odd` accordingly. It then calculates the sum of absolute differences between certain values derived from the loop iterations and the elements of `p`. Finally, it prints the minimum value between `even` and `odd`. The function does not explicitly state its purpose or return any values.

