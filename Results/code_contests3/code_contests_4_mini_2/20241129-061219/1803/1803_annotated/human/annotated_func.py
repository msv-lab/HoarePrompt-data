#State of the program right berfore the function call: The input is a string representing a set of small English letters formatted as "{letter1, letter2, ...}", where each letter is separated by a comma followed by a space, and the string starts with an opening curly bracket and ends with a closing curly bracket. The length of the input string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains the characters from `Cadena` at indices 1, 4, 7, ..., up to the length of `Cadena`, `k` is greater than or equal to the length of `Cadena` or `k` is equal to the length of `Cadena` plus 1.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string formatted as a set of small English letters enclosed in curly brackets, with letters separated by a comma and a space. It extracts every third character starting from the second character (index 1) of the input string and constructs a list of these characters. The function then computes and prints the number of unique characters found in this list. However, if the input string is formatted incorrectly (not starting with '{' or not containing enough characters), it may not process as intended. Additionally, the function does not handle cases where the input may be empty or not conforming to the expected format.

