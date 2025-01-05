#State of the program right berfore the function call: q is a positive integer (1 ≤ q ≤ 10^5) representing the number of queries, and each ni is a positive integer (1 ≤ ni ≤ 10^9) provided in the subsequent q lines.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer (1 ≤ q ≤ 10^5), `_` is `q - 1`, `ni` are the positive integers provided in the input, `c` is either 0 or 1 depending on the last processed `a`, and the outputs are either -1 or the calculated values based on `a` for each query.
#Overall this is what the function does:The function accepts a positive integer `q` representing the number of queries, and for each query, it processes a positive integer `a`. If `a` is odd, it subtracts 9 from it and sets a counter `c` to 1. Then, it checks if the modified `a` is in the set {1, 2, 3, 5, 7, 11}; if it is, it outputs -1. Otherwise, it computes and outputs `(a / 4) + c`. The function does not return any values; instead, it prints results directly for each query.

