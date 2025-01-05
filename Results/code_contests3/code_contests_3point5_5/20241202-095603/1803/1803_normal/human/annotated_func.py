#State of the program right berfore the function call: The input string contains a set of letters enclosed in opening and closing curved brackets. The length of the input string doesn't exceed 1000 characters.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` is a list containing the updated elements from `Cadena`, `k` is adjusted to be less than or equal to the new length of `Cadena`, `Cadena` length is greater than 2, the loop has finished
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string containing a set of letters enclosed in opening and closing curved brackets. It then extracts every third character from the input string and stores it in a list `Arreglo`. After processing, it prints the count of unique elements in the `Arreglo` list. The function does not explicitly return any value. The loop continues as long as the length of the input string is greater than the current index `k` and the length of the input string is greater than 2. However, there is a potential issue with the loop termination condition as it only considers the length of `Cadena` and not the length of `Arreglo` which may lead to unexpected behavior if the condition is not met.

