#State of the program right berfore the function call: There is a list of n positive integers representing stick lengths, where 1 <= n <= 1000 and 1 <= each stick length <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer where `1 <= n <= 1000`, `sticks` is a sorted list of `n` positive integers, `mid` is the stick length at index `n // 2` of `sticks`, `min_cost` is the minimum cost achievable by considering partitions around stick lengths from `mid - 1` down to `1`, and `min_t` is the stick length that yields `min_cost`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is an input integer where `1 <= n <= 1000`, `sticks` is a sorted list of `n` positive integers, `mid` is the stick length at index `n // 2` of `sticks`, `min_cost` is the minimum cost achievable by considering partitions around stick lengths from `mid` to `100`, and `min_t` is the stick length that yields `min_cost`.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts a list of positive integers representing stick lengths and returns the optimal stick length and the minimum cost achievable by considering partitions around this length. The function first sorts the input list in ascending order, then iterates through potential stick lengths from the middle value down to 1 and up to 100, calculating the minimum cost at each step. The minimum cost is determined by summing the minimum absolute differences between each stick length and the current potential stick length or its adjacent length. The function returns the optimal stick length and the corresponding minimum cost achievable, handling all input scenarios within the defined constraints (1 <= n <= 1000 and 1 <= each stick length <= 100) and edge cases such as empty lists or lists with a single element are implicitly handled by the input validation and iteration logic, though explicit error handling for these cases is not included in the provided code.

