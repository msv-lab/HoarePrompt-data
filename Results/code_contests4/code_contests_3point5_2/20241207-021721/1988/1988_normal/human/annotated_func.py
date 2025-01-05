#State of the program right berfore the function call: The input consists of multiple datasets, where each dataset contains 10 integers separated by blanks.**
def func():
    n = input()
    data = []
    for i in range(n):
        tmp = map(int, raw_input().split())
        
        data.append(tmp)
        
    #State of the program after the  for loop has been executed: `data` is a list of lists where each inner list contains integers parsed from user input, `n` is greater than or equal to 1, `i` is equal to `n-1` after the loop finishes
#Overall this is what the function does:The function `func` reads multiple datasets where each dataset consists of 10 integers separated by blanks. It stores these integers in a list of lists called `data`. The function does not explicitly return any value. It is important to note that the code uses `input()` and `raw_input()` functions which are not valid in Python 3, so the code may not run as expected in Python 3.

