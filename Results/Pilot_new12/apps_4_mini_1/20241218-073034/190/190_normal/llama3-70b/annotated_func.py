#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 1000 and a is a list of n integers where each integer represents a stick's length and satisfies 1 <= a[i] <= 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an input positive integer such that 1 <= `n` <= 1000; `a` is a list of `n` integers representing stick lengths within the range 1 <= `a[i]` <= 100; `sticks` is a sorted list of the integers in `a`; `mid` is at least 1; `min_cost` is the minimum cost calculated based on the evaluated values of `i` from `mid - 1` down to `1`; `min_t` is the value of `i` that corresponds to `min_cost` if the loop executed; if the loop did not execute, `min_t` remains equal to the initial value of `mid`.
    for i in range(mid + 1, 101):
        cost = sum(min(abs(x - i), abs(x - (i - 1))) for x in sticks)
        
        if cost < min_cost:
            min_cost = cost
            min_t = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 1000; `a` is a list of `n` integers representing stick lengths within the range 1 <= `a[i]` <= 100; `sticks` is a sorted list of the integers in `a`; `mid` is at most 99; `min_cost` is the minimum cost evaluated for stick lengths from `mid + 1` to `100`; `min_t` is the value of `i` that corresponds to the minimum cost found during the iterations, or remains equal to its initial value if no cost was found to be less than the initial `min_cost`.
    print(min_t, min_cost)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers representing stick lengths, sorts the lengths, and then calculates the minimum cost of adjusting stick lengths to a target length. It first considers the median of the stick lengths and then iteratively checks target lengths below and above this median (from `mid - 1` to `1` and from `mid + 1` to `100`) to find the target length `min_t` with the minimum cost. The final output includes `min_t` and the associated `min_cost`, which represents the least total effort required to adjust the sticks to a uniform length. It also handles edge cases for the output when there are no lengths below 1 or above 100. The function does not have any handling for when `n` is 0 or when input values are out of the specified bounds (though constraints are stated), but it assumes valid input as per the usage context.

