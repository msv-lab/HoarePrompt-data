#State of the program right berfore the function call: a and b are integers where a represents the number of rows (n) and b represents the number of columns (m) of the grid, and all of n, m, L, R are positive integers such that 1 ≤ n, m, L, R ≤ 10^9 and n * m ≥ 2.
def func_1(a, b):
    if (a > b) :
        return a - b
        #The program returns the difference between the integers 'a' and 'b', where 'a' represents the number of rows and is greater than 'b' which represents the number of columns.
    #State of the program after the if block has been executed: *`a` and `b` are integers where `a` represents the number of rows (n) and `b` represents the number of columns (m) of the grid, and all of `n`, `m`, `L`, `R` are positive integers such that 1 ≤ n, m, L, R ≤ 10^9 and n * m ≥ 2. Additionally, `a` is less than or equal to `b`.
    return b - a
    #The program returns the difference between the number of columns (b) and the number of rows (a), where a is less than or equal to b
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`, which represent the number of rows and columns of a grid, respectively. It returns the absolute difference between `a` and `b`. If `a` is greater than `b`, it returns `a - b`; otherwise, it returns `b - a`. The function effectively computes the difference regardless of which value is larger, ensuring a non-negative result.

