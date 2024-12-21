#State of the program right berfore the function call: The function func takes no arguments, but the program reads two lines of input where the first line is a single integer n (1 <= n <= 1000) and the second line contains n integers a_i (1 <= a_i <= 100).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000 (inclusive), `a` is a list of input integers, `min_cost` is the minimum cumulative adjustment based on the differences between elements of `a` and the value of `t`, `best_t` is the value of `t` that corresponds to the minimum cost, and `t` is 100.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts two lines of input through the program's standard input, with the first line containing a single integer n (1 <= n <= 1000) and the second line containing n integers a_i (1 <= a_i <= 100). It calculates and prints the value of t (between 1 and 100 inclusive) that minimizes the cumulative adjustment cost, based on the differences between each integer in the input list and the value of t, and the corresponding minimum cost. The cost is calculated as the sum of adjustments needed for each integer to be within the range [t-1, t+1], where integers less than t-1 are increased to t-1 and integers greater than t+1 are decreased to t+1. The function does not handle cases where the input is invalid (e.g., non-integer input or out-of-range integers), and it does not provide any error messages or handling for such cases. After execution, the function's state is reflected in its output, which is the value of t that corresponds to the minimum cost and the minimum cost itself, printed to the standard output.

