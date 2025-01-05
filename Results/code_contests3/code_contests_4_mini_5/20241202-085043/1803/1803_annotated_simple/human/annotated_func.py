#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, where letters are separated by a comma followed by a space, and the length of the string does not exceed 1000 characters. The string starts with an opening bracket '{' and ends with a closing bracket '}'.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: If len(Cadena) > 2, `Arreglo` contains the characters from `Cadena` at indices 1, 4, 7, ..., and `k` is greater than or equal to len(Cadena). If len(Cadena) <= 2, `Arreglo` is empty and `k` is 1.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string input representing a set of small English letters enclosed in curly brackets, where letters are separated by a comma followed by a space. It processes this string to extract characters at specific intervals (indices 1, 4, 7, etc.) and counts the number of unique characters from this subset. Finally, it prints the count of unique characters. If the input string is empty or consists of just the curly brackets, the function will result in an empty list and print `0`.

