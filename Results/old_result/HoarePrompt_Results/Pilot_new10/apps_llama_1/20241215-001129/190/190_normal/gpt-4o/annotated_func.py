#State of the program right berfore the function call: A list of positive integers representing stick lengths is provided, with the length of the list (n) being between 1 and 1000 (inclusive), and each stick length being between 1 and 100 (inclusive).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    min_cost = float('inf')
    best_t = -1
    for t in range(1, 101):
        current_cost = 0
        
        for length in a:
            if length < t - 1:
                current_cost += t - 1 - length
            elif length > t + 1:
                current_cost += length - (t + 1)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_t = t
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `a` is the original list of input integers between 1 and 100 (inclusive), `min_cost` is the minimum cost to adjust all lengths in `a` to be within a range of the form `[t-1, t+1]` for some `t` between 1 and 100, and `best_t` is the value of `t` that achieves this minimum cost.
    print(best_t, min_cost)
#Overall this is what the function does:The function reads a list of stick lengths from the user, calculates the target length that minimizes the total cost of adjusting the stick lengths to be within a range of the form [t-1, t+1], and prints the target length along with the minimum cost, handling all potential cases of stick length distributions.

