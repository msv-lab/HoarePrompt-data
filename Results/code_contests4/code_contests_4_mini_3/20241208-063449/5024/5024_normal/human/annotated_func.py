#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; the first permutation and the second permutation are lists of integers containing exactly the numbers 1 through n, each appearing exactly once.
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `start` is a list of integers with `n` elements; `start_m` is a dictionary mapping each unique value in `start` to its corresponding index in the list.
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `start` is a list of integers with `n` elements; `start_m` is a dictionary mapping each unique value in `start` to its corresponding index in the list; `end_m` contains the mapping of each unique value in `end` to its corresponding index; `end` is a list with `n` elements.
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `res` is the maximum number of moves needed to match indices between `start` and `end`, `start_m` is a mapping of unique values in `start` to their indices, `end_m` is a mapping of unique values in `end` to their indices, `start` is a list of integers with `n` elements, `end` is a list of integers with `n` elements.
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` and two permutations of integers from 1 to `n`. It calculates and returns the maximum number of moves required to align the indices of the elements in the first permutation (`start`) with those in the second permutation (`end`). The moves are calculated based on the difference in indices, considering wrapping around the list as needed.

