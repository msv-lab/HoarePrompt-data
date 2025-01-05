#State of the program right berfore the function call: n is an even integer greater than or equal to 2.**
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative even integer greater than or equal to 2, `p` is a list of integers where each element has been decremented by 1, `even` is the sum of absolute differences between the calculated values and p[i] for even indices i, `odd` is the sum of absolute differences between the calculated values and p[i] for odd indices i
    print(min(even, odd))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `p`, decrements each element of `p` by 1, calculates the sum of absolute differences between the calculated values and the corresponding elements in `p` for even and odd indices separately. It then prints the minimum value between the sums of even and odd indices. The function does not return any value.

