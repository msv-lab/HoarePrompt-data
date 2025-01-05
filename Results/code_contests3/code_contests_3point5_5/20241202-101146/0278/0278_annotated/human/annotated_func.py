#State of the program right berfore the function call: **n is an integer representing the number of ingredients, V is an integer representing the volume of the pan, ai is a list of n integers representing the proportions of ingredients, and bi is a list of n integers representing the available amounts of ingredients.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input for the number of ingredients `n`, the volume of the pan `V`, proportions of ingredients `a`, and available amounts of ingredients `b`. It then calculates a value based on the proportions and available amounts of ingredients, and prints the result. There is no specified return value.

