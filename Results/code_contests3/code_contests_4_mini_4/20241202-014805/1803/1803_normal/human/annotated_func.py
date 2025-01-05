#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, where letters are separated by a comma followed by a space, and the length of the string does not exceed 1000 characters. The string starts with an opening curly bracket and ends with a closing curly bracket.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is a string representing a set of small English letters, `Arreglo` contains every third element from `Cadena`, starting from the second element (index 1), `k` is greater than or equal to the length of `Cadena`.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads a string input formatted as a set of small English letters enclosed in curly brackets, extracts every third letter starting from the second one, counts the number of unique letters from that extraction, and prints the count. It does not handle malformed input or return any values.

