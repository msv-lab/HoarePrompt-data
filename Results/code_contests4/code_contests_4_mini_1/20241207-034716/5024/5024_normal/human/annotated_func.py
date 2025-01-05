#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; the first permutation and the second permutation are both lists of n unique integers, each containing numbers from 1 to n exactly once.
def func():
    n = int(sys.stdin.readline())
    start = [int(x) for x in sys.stdin.readline().split()]
    end = [int(x) for x in sys.stdin.readline().split()]
    start_m = {}
    for (index, val) in enumerate(start):
        start_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000, `start` is a list of integers with at least `n` elements, `start_m` is a dictionary mapping each element in `start` to its corresponding index.
    end_m = {}
    for (index, val) in enumerate(end):
        end_m[val] = index
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `start` is a list of integers with at least `n` elements; `start_m` is a dictionary mapping each element in `start` to its corresponding index; `end` is a list with at least `n` elements; `end_m` is a dictionary mapping each element in `end` to its corresponding index in the list.
    res = 0
    for (v1, i1) in start_m.items():
        i2 = end_m[v1]
        
        n_moves = i2 - i1
        
        if n_moves < 0:
            n_moves = n - i1
        
        res = max(res, n_moves)
        
    #State of the program after the  for loop has been executed: `res` is the maximum number of moves calculated based on the indices of elements in `start` and `end`, `n_moves` is the final calculated number of moves from the last iteration, `start_m` is a dictionary mapping elements in `start` to their indices, `end_m` is a dictionary mapping elements in `end` to their indices.
    print(res)
#Overall this is what the function does:The function reads a positive integer n and two permutations of unique integers from 1 to n. It calculates the maximum number of moves required to rearrange the first permutation into the second by shifting elements around in a circular manner. The function then prints this maximum number of moves. It does not accept parameters directly, as it reads input from standard input.

