#State of the program right berfore the function call: There exists a list of positive integers, which will be referred to as the stick lengths, where each integer is in the range of 1 to 100, and the count of stick lengths is in the range of 1 to 1000. This list of stick lengths will be provided as input to the function.
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
        
    #State of the program after the  for loop has been executed: `sticks` is a sorted list of positive integers, each in the range of 1 to 100, and the count of these stick lengths is in the range of 1 to 1000; `n` is an input integer that is at least 2 if the loop executes, or any integer if the loop does not execute; `mid` is the `n // 2`-th element in `sticks` and is at least 1; `t` is equal to `mid`; `min_cost` is the minimum sum of the minimum absolute differences between each stick length in `sticks` and either `i` or `i + 1` for any `i` from 1 to `mid`; `min_t` is the value of `i` that achieves this minimum sum.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `sticks` is a sorted list of positive integers, `n` is an integer, `mid` is the `n // 2`-th element in `sticks`, `t` equals `mid`, `min_cost` is the minimum sum of the minimum absolute differences between each stick length in `sticks` and either `i` or `i - 1` for any `i` from `mid + 1` to `100`, and `min_t` is the value of `i` that achieves this minimum sum.
    print(min_t, min_cost)
#Overall this is what the function does:The function accepts a list of stick lengths, calculates the median, and then finds the stick length that minimizes the sum of the minimum absolute differences between each stick length and either the current length or the adjacent length, printing this stick length and the corresponding minimum cost.

