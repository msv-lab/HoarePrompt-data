#State of the program right berfore the function call: The input is a string that starts with '{', ends with '}', and contains small English letters separated by ', '. The length of the string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is an input string that starts with '{', ends with '}', and has a length greater than 2; `Arreglo` contains the characters at indices 1, 4, 7, ..., up to the last valid index less than the length of `Cadena`; `k` is equal to the first index greater than or equal to the length of `Cadena` that would break the loop (which is greater than or equal to the length of `Cadena`)
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts an input string formatted as '{letter1, letter2, ...}' and extracts characters at indices 1, 4, 7, etc., from the string. It then computes and prints the number of unique characters extracted from these indices. If the input string does not meet the expected format or length requirements, the function may not behave as intended, such as returning 0 for empty or invalid inputs.

