#State of the program right berfore the function call: The input string is a set of letters enclosed in curly braces, separated by commas and spaces. The length of the input string is less than or equal to 1000 characters.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is a set of letters with a length greater than 2, `Arreglo` contains the second, fifth, and eighth letter of `Cadena`, `k` is 13, the loop will not execute again
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads a string input consisting of letters separated by commas and spaces. It then creates a list `Arreglo` containing specific letters from the input string based on the index pattern [1, 4, 7, ...]. The function then prints the count of unique letters in `Arreglo`. The function does not have a return value.

