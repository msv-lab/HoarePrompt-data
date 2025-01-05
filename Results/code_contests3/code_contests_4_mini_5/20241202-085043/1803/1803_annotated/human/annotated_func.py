#State of the program right berfore the function call: The input is a string that starts with '{', ends with '}', and contains small English letters separated by ', '. The length of the string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is an input string that starts with '{', ends with '}', and contains small English letters separated by ', '; `Arreglo` contains every third element of `Cadena` starting from the second element; `k` is greater than the length of `Cadena` or invalid for further indexing.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string formatted as '{letter1, letter2, ...}' and processes it to collect every third character (starting from the first character after the opening brace) into a list. It then prints the count of unique letters from that list. However, the function does not return any value; it only prints the result. Additionally, it does not handle malformed input strings or strings that do not follow the expected format.

