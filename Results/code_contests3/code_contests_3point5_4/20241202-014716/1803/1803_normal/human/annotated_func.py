#State of the program right berfore the function call: The input string represents a set of letters enclosed in curly brackets, separated by commas and spaces.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains the elements at indexes 1, 4, 7, ... of `Cadena`, `k` is such that for the loop to execute again, `len(Cadena) <= k` or `len(Cadena) <= 2`
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads an input string representing a set of letters enclosed in curly brackets, separated by commas and spaces. It then extracts every third character starting from index 1 in the input string and prints the number of unique characters extracted. The function does not accept any parameters.

