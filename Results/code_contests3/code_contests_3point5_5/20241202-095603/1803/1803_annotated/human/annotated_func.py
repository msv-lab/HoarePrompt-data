#State of the program right berfore the function call: The input string contains small English letters separated by commas and enclosed within opening and closing curved brackets. The length of the input string doesn't exceed 1000.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` contains small English letters separated by commas and enclosed within opening and closing curved brackets, with a length greater than 11 and greater than 2; `k` is 11; `Arreglo` contains the appended elements from `Cadena` at indexes 5, 8, and 11
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string containing small English letters separated by commas and enclosed within opening and closing curved brackets. It then extracts elements from specific indexes in the input string and stores them in a list `Arreglo`. The function then prints the count of unique elements in `Arreglo`. The function does not explicitly return a value.

