#State of the program right berfore the function call: The input consists of a set of letters enclosed in curly brackets, separated by commas and spaces. The length of the input line does not exceed 1000 characters.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: Cadena is a set of letters enclosed in curly brackets, separated by commas and spaces; Arreglo is a list containing elements at indexes 4, 5, 8, 9, 12, 13, ... of Cadena; k is increased by 3 until the loop condition is no longer met
    print(len(list(set(Arreglo))))
#Overall this is what the function does:Functionality: The function `func` reads a line of input consisting of a set of letters enclosed in curly brackets, separated by commas and spaces. It then creates a list `Arreglo` containing elements at specific indexes of the input line based on the loop condition. Finally, it prints the count of unique elements in `Arreglo`. The function does not accept any parameters and does not return any value. It may have potential issues related to input validation and data processing as the code retrieves specific elements from the input line based on fixed indexes without thorough validation.

