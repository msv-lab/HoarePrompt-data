#State of the program right berfore the function call: Each dataset consists of 10 integers separated by blanks.**
def func():
    n = input()
    data = []
    for i in range(n):
        tmp = map(int, raw_input().split())
        
        data.append(tmp)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `data` is a list containing a total of n lists, each list containing integers mapped from input split by whitespace, `tmp` contains the last list of integers mapped from input split by whitespace
#Overall this is what the function does:The function `func` reads an integer `n` as input and then reads `n` lines, each containing 10 integers separated by whitespace. It stores these integers in a list of lists named `data`. The function does not accept any parameters and solely relies on user input to populate the `data` list. The purpose or specific functionality of the function beyond this input processing is not defined and would need to be clarified based on additional information or constraints.

