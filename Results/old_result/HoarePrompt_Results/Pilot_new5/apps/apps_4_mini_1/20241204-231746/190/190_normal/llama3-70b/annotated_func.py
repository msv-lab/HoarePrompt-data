#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000, and a is a list of n integers where each integer a_i is a positive integer such that 1 <= a_i <= 100.
def func():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    mid = sticks[n // 2]
    cost = sum(abs(x - mid) for x in sticks)
    t = mid
    min_cost = cost
    min_t = t
    for i in range(mid - 1, 0, -1):
        cost = sum(min(abs(x - i), abs(x - (i + 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 1000, `a` is a list of `n` positive integers such that 1 <= `a_i` <= 100, `sticks` is a sorted list of `n` integers, `mid` is at least 1, `t` is equal to `mid`, `min_cost` is the minimum cost calculated from all iterations, and `min_t` is the value of `i` that corresponds to `min_cost`, if the loop executed; otherwise, `min_t` remains `mid`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 1000, `a` is a list of `n` positive integers such that 1 <= `a_i` <= 100, `sticks` is a sorted list of `n` integers, `mid` is less than or equal to 99, `t` equals `mid`, `min_cost` is the minimum cost calculated for all values of `i` from `mid + 1` to 100, and `min_t` is the value of `i` that corresponds to `min_cost`, or remains equal to `mid` if the loop did not execute.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 1000) and a list of `n` integers where each integer is a positive integer (1 <= a_i <= 100). It sorts the list and calculates the minimum cost to move all integers to a specific target value, `min_t`, which is determined to minimize the total cost. The function then prints `min_t`, which is the optimal target value, and `min_cost`, the corresponding minimum cost. The function handles target values both below and above the median of the sorted list, ensuring it explores the range from 1 to 100.

