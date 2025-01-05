#State of the program right berfore the function call: The input is a string that starts with an opening curly bracket '{' and ends with a closing curly bracket '}', containing small English letters separated by a comma and a space, or is an empty set represented by '{}'. The length of the string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains elements `Cadena[1], Cadena[4], Cadena[7], ...` up to the last valid index before exceeding the length of `Cadena`; `k` is greater than `len(Cadena)` at termination.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string input that represents a set of small English letters formatted with curly brackets, such as '{a, b, c}', or is an empty set represented by '{}'. It extracts every third character starting from the second character (index 1) of the input string, counts the unique letters from the extracted characters, and prints the count. If the input does not conform to the expected format or is an empty set, the function may not behave as intended, potentially leading to an output of 0 for an empty set.

