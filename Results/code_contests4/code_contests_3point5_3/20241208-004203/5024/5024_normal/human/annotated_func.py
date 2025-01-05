#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5.**
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an integer, `start` is a list containing integers, `end` is a list containing integers, `start_m` is a dictionary with key-value pairs where the keys are elements from the `start` list and the values are their corresponding indices
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is an integer, `start` is a list containing integers, `end` is a list containing integers, `start_m` is a dictionary with key-value pairs, `end_m` is a dictionary with key-value pairs where the keys are elements from the `end` list and the values are their corresponding indices
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `start` is a list of integers, `end` is a list of integers, `start_m` has key-value pairs, `end_m` is a dictionary with key-value pairs, `res` is the maximum difference between corresponding values from `start_m` and `end_m`
    print(res)
#Overall this is what the function does:The function `func` reads an integer `n` from standard input, followed by two lists of integers `start` and `end`. It then creates dictionaries `start_m` and `end_m` with key-value pairs of elements and their corresponding indices from the lists. The function calculates the maximum difference between the indices of corresponding elements in the two dictionaries and prints this maximum difference. The function does not accept any parameters and does not return any value.

