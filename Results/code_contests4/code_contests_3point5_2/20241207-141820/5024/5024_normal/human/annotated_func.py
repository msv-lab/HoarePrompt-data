#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5.**
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 2*10^5, `start` is a list of integers obtained from input, `end` is a list of integers obtained from input, `start_m` is a dictionary with key `val` and value `index` where `val` is each element in the `start` list and `index` is the index of that element in the `start` list
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an integer, `start` is a list of integers, `end` is a list of integers, `start_m` is a dictionary with key `val` and value `index`, `end_m` is a dictionary with each element in the `end` list as key and the corresponding index as its value
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `start` is a list of integers, `end` is a list of integers, `start_m` is a dictionary with keys and corresponding indices, `end_m` is a dictionary with each element in the `end` list as key and the corresponding index as its value, `res` is the maximum value of all calculated `n_moves` after iterating through all key-value pairs in `start_m`
    print(res)
#Overall this is what the function does:The function `func` reads input from the user, processes the input to create dictionaries from lists, calculates the maximum number of moves between corresponding elements in the input lists, and prints the result. The function does not accept any parameters and does not return any value.

