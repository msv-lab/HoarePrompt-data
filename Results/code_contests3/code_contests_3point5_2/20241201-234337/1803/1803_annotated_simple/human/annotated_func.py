#State of the program right berfore the function call: The input string contains a set of letters enclosed in curly braces, separated by commas and spaces.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains elements from `Cadena[1]` to `Cadena[k]` where `k` is the last index less than the length of `Cadena` that is a multiple of 3, `k` is the last value of `k` before the loop condition becomes false
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string that contains a set of letters enclosed in curly braces, separated by commas and spaces. It then creates a list `Arreglo` by extracting elements from the input string based on a specific pattern. The function prints the number of unique elements in `Arreglo`. The function does not accept any parameters and does not return a specific output.

