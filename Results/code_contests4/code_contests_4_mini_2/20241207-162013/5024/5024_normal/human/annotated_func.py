#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), the first permutation is a list of n unique integers from 1 to n, and the second permutation is also a list of n unique integers from 1 to n.
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `start_m` is a dictionary mapping each unique value in `start` to its index, `n` is a positive integer (1 ≤ n ≤ 200,000), `start` is a list of integers with at least n elements.
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `start_m` is a dictionary mapping each unique value in `start` to its index; `n` is a positive integer (1 ≤ n ≤ 200,000); `start` is a list of integers with at least n elements; `end` is a list with at least as many elements as there are unique values in `end`; `end_m` is a dictionary mapping each unique value in `end` to its index in `end`.
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `start_m` is a dictionary mapping each unique value in `start` to its index; `end_m` is a dictionary mapping each unique value in `end` to its index; `res` is the maximum number of moves calculated based on the differences between indices of corresponding values in `start` and `end`, considering the circular nature of the list; `n` is a positive integer (1 ≤ n ≤ 200,000).
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` and two permutations of unique integers from 1 to `n`. It calculates the maximum number of moves required to align the indices of the two permutations, considering the circular nature of the list. The function prints this maximum number of moves, but does not return any value.

