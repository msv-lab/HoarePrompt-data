#State of the program right berfore the function call: The input string represents a set of small English letters enclosed in opening and closing curved brackets. The length of the input string doesn't exceed 1000. Each letter is separated by a comma and a space.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is assigned the input string representing a set of small English letters enclosed in opening and closing curved brackets; `Arreglo` contains the elements at index 4, 7, 10, ... of the original `Cadena` string based on the value of `k` in each iteration; `k` is such that `k + 3` is greater than the length of `Cadena` for the loop to terminate
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads an input string representing a set of small English letters enclosed in brackets. It then extracts and prints the unique letters at specific positions in the string based on the value of `k`. The output is the count of unique letters extracted. If the input string length is less than or equal to 2, or if `k + 3` never exceeds the length of the input string, the function may not extract any letters or may not terminate properly.

