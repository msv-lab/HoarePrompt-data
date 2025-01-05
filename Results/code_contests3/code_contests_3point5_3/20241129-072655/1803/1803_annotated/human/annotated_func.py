#State of the program right berfore the function call: The input string contains small English letters separated by a comma, starting with an opening curved bracket and ending with a closing curved bracket.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` is a list containing the elements `Cadena[1]`, `Cadena[4]`, `Cadena[7]`, ..., `Cadena[n]` where n is the last index that satisfies the loop condition, `k` is the value that caused the loop to terminate
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string from the user. It then iterates over the string, extracting characters at specific indices according to the loop condition. The function constructs a list `Arreglo` containing these extracted characters. Finally, it prints the count of unique elements in the list `Arreglo`. The function does not take any parameters and the input string must contain small English letters separated by commas within brackets. However, the function does not return any value, and it does not have explicit constraints or relationships between input parameters.

