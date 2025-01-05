#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni, ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer such that 1 ≤ `q` ≤ 10^5; for each query `a`, `c` is either 0 or 1 based on the oddity of `a`, and the output will be either -1 or calculated as `a / 4 + c` depending on the value of `a`.
#Overall this is what the function does:The function accepts a positive integer `q` representing the number of queries. For each query `a`, it checks if `a` is odd and, if so, subtracts 9 from `a`. It then returns -1 if `a` is in the set {1, 2, 3, 5, 7, 11}. Otherwise, it returns the result of `a / 4 + c`, where `c` is 1 if `a` was odd and 0 if `a` was even. This function effectively processes up to 100,000 queries, each being a positive integer up to 1 billion, and produces the corresponding output based on the defined conditions.

