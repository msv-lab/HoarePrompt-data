#State of the program right berfore the function call: The input string is a set of letters enclosed in curly brackets, with each letter separated by a comma and a space. The length of the input string does not exceed 1000 characters.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Arreglo` contains the elements at indexes 1, 4, 7, 10, ... of `Cadena`, `k` is 13, for the loop to execute `k` should be less than the new length of `Cadena`
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function `func` reads an input string containing letters separated by commas and spaces, extracts specific elements from the string based on their indexes, and then prints the count of unique elements extracted. The function does not accept any parameters explicitly, but it reads the input string from the user. The extracted elements are based on the pattern of selecting every third element starting from the second element. If the input string is less than 3 characters long or the loop condition does not allow further iterations, the function may not extract any elements.

