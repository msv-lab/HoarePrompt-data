#State of the program right berfore the function call: x is an integer representing the number of participants (1 ≤ x ≤ 500), b is an integer representing the number of bottles of water required for each participant per match (1 ≤ b ≤ 500), and p is an integer representing the number of towels given to each participant for the whole tournament (1 ≤ p ≤ 500).
def func_1(x):
    for i in range(10):
        if potencias[i] > x:
            return potencias[i - 1]
        
    #State of the program after the  for loop has been executed: Output State:
#Overall this is what the function does:The function `func_1` accepts an integer `x` and returns a specific value from the list `potencias`. Specifically:
- If there exists an index `i` such that `potencias[i]` is greater than `x`, the function returns `potencias[i - 1]`.
- If no such `i` exists, the function returns `potencias[0]`.
- If `potencias[2]` is greater than `x`, the function returns `potencias[2]`. Otherwise, it does not return anything.

