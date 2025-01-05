#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, where the letters are separated by commas followed by a space, and the length of the string does not exceed 1000 characters. The string starts with '{' and ends with '}'.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: 'Cadena' is a string representing a set of small English letters, 'Arreglo' contains every third character from 'Cadena' starting from the second character, 'k' is equal to the length of 'Cadena' or greater, depending on the initial length of 'Cadena'
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads a string input formatted as a set of small English letters enclosed in curly brackets, extracts every third character starting from the second character, and prints the count of unique characters from this extracted list. It does not return any value and does not handle malformed input properly.

