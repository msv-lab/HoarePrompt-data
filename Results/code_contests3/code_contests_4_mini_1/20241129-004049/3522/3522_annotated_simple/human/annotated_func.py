#State of the program right berfore the function call: q is a positive integer representing the number of queries, and for each query, ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer greater than or equal to 1; `a` is the last input value processed, which can be either odd or even; `c` is either 1 (if the last `a` was odd) or 0 (if the last `a` was even); the output for the last query is either -1 or the result of the last `a / 4 + c`.
#Overall this is what the function does:The function accepts a positive integer input representing the number of queries and processes each query with a positive integer `ni` (1 ≤ ni ≤ 10^9). For each input value `a`, if `a` is odd, it subtracts 9 from it and sets a flag `c` to 1; otherwise, `c` remains 0. The function then checks if the modified or original value of `a` is one of the small primes (1, 2, 3, 5, 7, 11) and returns -1 if so. If not, it returns the result of `a / 4 + c`. This means the function can return -1 for certain small prime values and calculates a value based on division and conditionally set flags for odd inputs. The function does not return any values explicitly but prints the results directly to the output for each query.

