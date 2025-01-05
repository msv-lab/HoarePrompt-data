#State of the program right berfore the function call: The input string contains a set of small English letters separated by commas and enclosed in opening and closing curved brackets. The length of the input string is not more than 1000 characters.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: Cadena` is a string containing at least 3 small English letters separated by commas and enclosed in brackets, `Arreglo` contains the second letter of `Cadena` followed by every third letter of `Cadena`, `k` is the value that makes the loop condition false, which is greater than or equal to the length of `Cadena`
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string containing small English letters separated by commas and enclosed in brackets. It then extracts the second letter of the input string followed by every third letter. The function then prints the number of unique letters in the extracted sequence. The function does not return any specific value.

