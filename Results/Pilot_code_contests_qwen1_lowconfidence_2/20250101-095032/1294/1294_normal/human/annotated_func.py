#State of the program right berfore the function call: x is an integer representing the number of participants (1 ≤ x ≤ 500), b is an integer representing the number of bottles of water required for each participant per match (1 ≤ b ≤ 500), and p is an integer representing the number of towels given to each participant for the whole tournament (1 ≤ p ≤ 500).
def func_1(x):
    for i in range(10):
        if potencias[i] > x:
            return potencias[i - 1]
        
    #State of the program after the  for loop has been executed: `x` is an integer representing the number of participants (1 ≤ x ≤ 500), `b` is an integer representing the number of bottles of water required for each participant per match (1 ≤ b ≤ 500), `p` is an integer representing the number of towels given to each participant for the whole tournament (1 ≤ p ≤ 500), `i` is 10, and if `potencias[i]` is greater than `x`, the function returns `potencias[9]`. Otherwise, the function does not return anything.
#Overall this is what the function does:The function `func_1` accepts a single parameter `x` which is an integer representing the number of participants (1 ≤ x ≤ 500). It iterates through a predefined list `potencias` of length 10. If `x` is less than or equal to the value at index 9 in `potencias`, the function does not return anything. If `x` is greater than the value at index 9 but less than or equal to the value at index 8, the function returns the value at index 9. For all other values of `x`, the function returns the value at index 0. This means the function essentially maps the input `x` to one of three possible outputs based on its value relative to the values in the `potencias` list.

