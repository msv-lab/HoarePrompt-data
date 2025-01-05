#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5.**
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `start` is a list of integers with at least 1 element, `end` is a list of integers created by converting input from standard input into integers, `start_m` is a dictionary with all elements in `start` as keys and their corresponding indices as values
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `start` is a list of integers with at least 1 element, `end` is a list of integers created by converting input from standard input into integers with at least 1 element, `start_m` is a dictionary with all elements in `start` as keys and their corresponding indices as values, `end_m` is a dictionary with the value of `val` from `end` list as key and `index` as its value, `index` is equal to the index of the last element in `end`, `val` is the last element in the `end` list
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `n`, `start`, `end`, `start_m`, `end_m`, `res`, `i2`, `n_moves` are all defined as described. The final value of `res` is the maximum number of moves required to reach from the starting position to the ending position in the lists, considering wrapping around if needed.
    print(res)
#Overall this is what the function does:The function `func` reads an integer `n` from standard input and two lists of integers `start` and `end`. It then constructs dictionaries `start_m` and `end_m` mapping values to their indices. The function calculates the maximum number of moves required to reach from the starting position to the ending position in the lists, considering wrapping around if needed, and prints the result. The function does not have a return statement and relies on global variables for its operation. The code does not handle cases where the input constraints are violated or if there are missing input values.

