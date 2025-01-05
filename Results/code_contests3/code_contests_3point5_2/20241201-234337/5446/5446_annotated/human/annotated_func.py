#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integers from the user input, calculates a value based on these inputs, and then prints the result after performing mathematical operations. However, the annotations mention that the function does not accept any parameters, which is incorrect as it clearly reads input values. Additionally, the annotations do not specify the expected output of the function. Therefore, the functionality should include that the function accepts user input, performs calculations, and prints the result.

