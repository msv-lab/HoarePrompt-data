#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and a is a list of n integers such that 1 ≤ a_i ≤ 100 for all i.
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
        
    #State of the program after the  for loop has been executed: `t` is 100, `n` is an integer such that \(1 \leq n \leq 1000\), `a` is a list of integers with length `n`, each element is between 1 and 100, `current_cost` is the final calculated cost based on the loop conditions, `min_cost` is the minimum value of `current_cost` encountered during the loop, and `best_t` is the value of `t` when `min_cost` is achieved.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts an integer \( n \) such that \( 1 \leq n \leq 1000 \) and a list \( a \) of \( n \) integers where each integer \( a_i \) satisfies \( 1 \leq a_i \leq 100 \). It then iterates over possible values of \( t \) from 1 to 100, calculating a cost for each \( t \) based on the differences between \( t \) and the elements in \( a \). The cost is defined such that if an element \( a_i \) is less than \( t - 1 \), the cost is increased by \( t - 1 - a_i \), and if \( a_i \) is greater than \( t + 1 \), the cost is increased by \( a_i - (t + 1) \). After evaluating all possible \( t \), the function identifies the value of \( t \) that results in the minimum cost and prints this value along with the corresponding minimum cost. If there are multiple values of \( t \) that result in the same minimum cost, the function will still identify one of them.

