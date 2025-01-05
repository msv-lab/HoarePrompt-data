#State of the program right berfore the function call: The input is a string that starts with an opening curly bracket '{', ends with a closing curly bracket '}', and contains lowercase English letters separated by a comma and a space. The length of the string does not exceed 1000 characters.
def func():
    Cadena = raw_input()
    Arreglo = []
    k = 1
    while len(Cadena) > k and len(Cadena) > 2:
        Arreglo = Arreglo + [Cadena[k]]
        
        k = k + 3
        
    #State of the program after the loop has been executed: `k` is greater than or equal to the length of `Cadena` divided by 3, `Arreglo` contains every third character from `Cadena` starting from the first character after the initial '{', and if `Cadena` initially contained more than 2 characters, then `Arreglo` will have elements; otherwise, it will remain empty.
    print(len(list(set(Arreglo))))
#Overall this is what the function does:The function accepts a formatted string of lowercase letters contained within curly brackets, extracts every third character starting from the first character after the opening bracket, and prints the number of unique characters from that extracted set. If the input string does not contain more than 2 characters, it will not extract any characters, resulting in a count of zero unique characters.

