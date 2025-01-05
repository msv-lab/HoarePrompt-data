#State of the program right berfore the function call: There are multiple datasets where the first line contains a positive integer N (the number of datasets), followed by N lines each containing exactly 10 integers, representing the sequence of balls dropped through the opening A. Each integer is a positive number.
def func():
    n = input()
    data = []
    for i in range(n):
        tmp = map(int, raw_input().split())
        
        data.append(tmp)
        
    #State of the program after the  for loop has been executed: `n` is an input string representing a number; `data` is a list containing all the mapped integers from the input for `n` datasets; `i` is `n-1` after the last iteration; `tmp` is a map object containing the integers from the last input string processed.
#Overall this is what the function does:The function accepts user input for the number of datasets and reads multiple lines, each containing exactly 10 positive integers, storing these integers in a list. The function does not return any value or output, and it does not handle any potential input errors such as non-integer values or incorrect numbers of integers per line.

