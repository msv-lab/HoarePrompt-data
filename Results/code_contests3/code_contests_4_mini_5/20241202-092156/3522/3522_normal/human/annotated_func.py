#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni (1 ≤ ni ≤ 10^9), ni is a positive integer.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is the last processed input value, `c` is either 0 or 1 depending on the parity of the last `a`, and the output is the last printed value based on the last processed `a`.
#Overall this is what the function does:The function accepts a positive integer `q` representing the number of queries and processes each query `a` (a positive integer). For each query, if `a` is odd, it subtracts 9 from `a` and increments a counter `c`. It then evaluates `a`: if `a` is one of the specific small primes (1, 2, 3, 5, 7, 11), it returns -1; otherwise, it returns the integer division of `a` by 4 plus `c`. The function does not explicitly handle cases where `a` is less than 9 correctly, as the logic may lead to unexpected results, and it lacks checks for input validity beyond the given constraints.

