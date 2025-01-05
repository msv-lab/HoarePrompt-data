#State of the program right berfore the function call: n is a positive integer representing the number of ingredients, V is a positive integer representing the volume of the pan, ai are positive integers representing the proportions of ingredients, and bi are non-negative integers representing the available amounts of ingredients.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function reads input for the number of ingredients and volume of the pan, as well as the proportions and available amounts of ingredients. It then calculates if there are enough ingredients to make the recipe based on the proportions and available amounts, and prints the result. However, the code snippet provided seems to have an issue with indentation and syntax errors, making it difficult to determine the exact functionality without correction. Additionally, the annotations are not aligned with the code, so the actual functionality might differ from the described annotations.

