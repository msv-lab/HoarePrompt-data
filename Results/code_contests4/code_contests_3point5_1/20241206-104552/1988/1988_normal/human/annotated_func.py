#State of the program right berfore the function call: The input consists of N datasets, where N is a positive integer. Each dataset contains 10 numbers separated by blanks.**
def func():
    n = input()
    data = []
    for i in range(n):
        tmp = map(int, raw_input().split())
        
        data.append(tmp)
        
    #State of the program after the  for loop has been executed: `n` is a string containing 10 numbers separated by blanks, `data` contains a list of 10 lists, each with integers extracted from the input, `i` is n-1
#Overall this is what the function does:The function `func` reads an input consisting of N datasets, where N is a positive integer. Each dataset contains 10 numbers separated by blanks. The function then processes these datasets by storing them in a list of lists within the `data` variable. The function does not explicitly return any value. It reads the number of datasets, reads the 10 numbers in each dataset, and stores them in a list of lists.

