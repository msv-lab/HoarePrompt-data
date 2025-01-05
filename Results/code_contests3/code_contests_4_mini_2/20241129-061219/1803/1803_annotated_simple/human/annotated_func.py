#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, with letters separated by commas and spaces. The string is guaranteed to start with '{' and end with '}', and its length does not exceed 1000.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `k` is greater than or equal to the length of `Cadena`, `Arreglo` contains elements from `Cadena` at every third index starting from index 1, provided the length of `Cadena` is greater than 2.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads a string input formatted as a set of small English letters enclosed in curly brackets, extracts letters at every third index starting from index 1, and prints the number of unique letters from this subset. The function does not handle cases where the input does not conform to the expected format, nor does it return any values; it only prints the result.

