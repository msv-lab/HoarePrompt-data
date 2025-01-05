#State of the program right berfore the function call: q is a positive integer representing the number of queries, and each ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer representing the number of queries, each `a` is a positive integer input, `c` is 1 for odd `a` and 0 for even `a`, and the final output for each query is either -1 if `a` is in (1, 2, 3, 5, 7, 11) or `a / 4 + c` otherwise.
#Overall this is what the function does:The function accepts a positive integer `q` representing the number of queries, and for each query processes a positive integer `a`. If `a` is odd, it subtracts 9 from `a` and sets `c` to 1; if `a` is even, `c` remains 0. The function then checks if `a` is in the set {1, 2, 3, 5, 7, 11} and returns -1 in that case. If not, it returns the value of `a / 4 + c`. This function handles a series of queries and modifies the output based on the conditions applied to each input integer. Edge cases include handling very small values of `a` and ensuring that the function properly calculates results for both odd and even integers.

