#State of the program right berfore the function call: The input string contains small English letters separated by commas, starting with an opening curved bracket and ending with a closing curved bracket. Each comma is followed by a space. The length of the input string doesn't exceed 1000.**
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `Cadena` is the input string containing small English letters separated by commas, `Arreglo` is the array containing every 4th element of `Cadena`, `k` is such that `len(Cadena) <= k or k = len(Cadena)`
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function reads an input string containing small English letters separated by commas within curved brackets. It then extracts every 4th element from the input string and stores them in an array. Finally, it prints the count of unique elements in that array.

