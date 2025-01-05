#State of the program right berfore the function call: n is a positive integer representing the number of ingredients, V is a positive integer representing the volume of the pan, ai and bi are positive integers representing the proportions and available amounts of ingredients respectively.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function reads input for the number of ingredients, volume of the pan, proportions, and available amounts. It then calculates and prints the total amount of each ingredient needed to fill the pan to the desired volume V based on the proportions and available amounts.

