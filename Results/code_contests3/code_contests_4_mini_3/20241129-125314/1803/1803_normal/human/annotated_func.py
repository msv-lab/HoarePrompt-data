#State of the program right berfore the function call: The input is a string representing a set of small English letters enclosed in curly brackets, with letters separated by a comma and a space. The string has a length no greater than 1000 characters. It is guaranteed to start with an opening curly bracket and end with a closing curly bracket.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `k` is greater than or equal to the length of `Cadena`, `Arreglo` contains every third character from `Cadena` starting from index 1, based on the initial `Cadena` input.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string input representing a set of lowercase English letters enclosed in curly brackets, processes it to extract every third character starting from the second character (index 1), and prints the count of unique characters from this extracted set. If the input string is not properly formatted or does not contain enough characters, the output will depend on the characters present but will always result in a count of unique letters. Note that the function does not return any value; it only prints the result.

