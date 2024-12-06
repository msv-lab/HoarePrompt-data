#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, and a is a list of n integers where each integer a_i is in the range 1 <= a_i <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 1000; `a` is a list of `n` integers where each integer `a_i` is in the range 1 <= `a_i` <= 100; `min_cost` is the minimum cost calculated over all values of `t` from 1 to 100; `best_t` is the value of `t` that resulted in `min_cost`; `current_cost` is the cost calculated for the last value of `t`, and `length` is the last integer processed from the list `a`.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of `n` integers, where `1 <= n <= 1000` and each integer in `a` is between `1` and `100`. It calculates the minimum cost required to adjust the values in `a` so that they all lie within the range `[t - 1, t + 1]` for `t` ranging from `1` to `100`, and returns the value of `t` that results in the minimum cost along with that minimum cost. The function prints `best_t` and `min_cost` as the output.

