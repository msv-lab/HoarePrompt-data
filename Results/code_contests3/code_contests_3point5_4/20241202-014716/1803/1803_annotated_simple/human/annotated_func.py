#State of the program right berfore the function call: The input line contains a set of small English letters enclosed within opening and closing curved brackets, separated by commas and spaces. The length of the line doesn't exceed 1000.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` remains unchanged, `Arreglo` contains the elements added from `Cadena` according to the loop conditions, `k` is such that `len(Cadena) <= k`
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads a line of input containing a set of small English letters separated by commas and spaces. It then iterates through the input and extracts elements based on specific conditions into a list. Finally, it prints the count of unique elements in the list. The function does not accept any parameters and does not return any value.

