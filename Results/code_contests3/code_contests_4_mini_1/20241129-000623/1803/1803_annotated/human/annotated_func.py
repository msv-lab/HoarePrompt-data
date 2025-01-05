#State of the program right berfore the function call: The input is a string that represents a set of small English letters, starting with '{' and ending with '}', with letters separated by ', '. The length of the input string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: 'Cadena' is a string of the format '{a, b}', 'Arreglo' contains elements from 'Cadena' at indices 1, 4, 7, ..., and 'k' is greater than or equal to len(Cadena).
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string input formatted as a set of lowercase English letters enclosed in curly braces (e.g., '{a, b}'). It extracts the letters at indices 1, 4, 7, etc., from the input string, counts the number of unique letters, and prints that count. The function does not return any value, and it assumes the input is well-formed according to the specified format. If the input does not follow this format or is empty, the function may not behave as expected.

