#State of the program right berfore the function call: The input string consists of small English letters separated by commas, enclosed by opening and closing curved brackets.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: Cadena is a string containing small English letters separated by commas, Arreglo contains the values at indices k, k+3, k+6, k+9, ..., until k exceeds the length of Cadena. k will be greater than the length of Cadena or 2, whichever is smaller
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads an input string containing English letters separated by commas and stores specific elements in a list based on certain indices. It then prints the number of unique elements in that list. The function does not have any return value.

