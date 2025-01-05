#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, with letters separated by a comma and a space, and the length of the string does not exceed 1000 characters. The string always starts with '{' and ends with '}'.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: 'k' is greater than or equal to the length of 'Cadena', 'Arreglo' contains the characters from 'Cadena' at indices 1, 4, 7, ... up to the last valid index accessible before 'k' exceeds 'len(Cadena)'. If 'len(Cadena)' is less than or equal to 2, 'Arreglo' is empty.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string input representing a set of lowercase letters enclosed in curly brackets, extracts unique letters from every third position starting from the second character, and prints the count of these unique letters. If the input is invalid or too short, it may produce unexpected results.

