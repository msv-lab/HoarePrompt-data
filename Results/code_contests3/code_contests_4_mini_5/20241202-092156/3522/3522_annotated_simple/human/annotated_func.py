#State of the program right berfore the function call: q is a positive integer representing the number of queries, and for each query, ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer representing the number of queries, `a` is the last input integer, `c` is 1 if the last `a` was odd (and modified), otherwise `c` is 0; the output for each query is either -1 if `a` is in (1, 2, 3, 5, 7, 11) or calculated as `a / 4 + c`.
#Overall this is what the function does:The function accepts a positive integer `q` which represents the number of queries. For each query, it takes a positive integer `a`. If `a` is odd, it is decremented by 9 and a counter `c` is set to 1. The function then checks if the modified or original `a` is in the set {1, 2, 3, 5, 7, 11}. If it is, it returns -1; otherwise, it returns the result of `a / 4 + c`. Therefore, it processes each query and outputs either -1 or a computed value based on the input integer.

