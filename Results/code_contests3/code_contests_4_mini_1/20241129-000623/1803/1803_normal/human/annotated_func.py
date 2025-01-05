#State of the program right berfore the function call: The input is a string representing a set of small English letters formatted as '{letter1, letter2, ...}' where each letter is separated by a comma followed by a space, and the string has a length of at most 1000 characters. The set may contain duplicate letters and can also be empty.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains the characters at positions 1, 4, 7, ... from the original `Cadena` until `k` exceeds the length of `Cadena`, `k` is the first value greater than or equal to the length of `Cadena` that is reached by incrementing by 3 starting from 1.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a string formatted as '{letter1, letter2, ...}' representing a set of small English letters. It extracts characters from this string at positions 1, 4, 7, etc., until it exceeds the length of the string. It then calculates and prints the number of unique letters extracted. The function does not validate the input format or handle any potential errors that may arise from invalid input.

