#State of the program right berfore the function call: q is a list of tuples where each tuple contains two integers (n, x) representing Vasya's position in the line and the number Vasya received during the settling, respectively, with the constraints 1 ≤ x < n ≤ 10^9. The length of q is between 1 and 100, inclusive.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is a list of tuples where each tuple contains two integers (n, x) representing Vasya's position in the line and the number Vasya received during the settling, respectively, with the constraints 1 ≤ x < n ≤ 10^9. The length of `q` is between 1 and 100, inclusive. If `w` equals its integer division by 1 and `w` is greater than or equal to `x - 1`, then `M` is a list containing one element, `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: 
    return M
    #The program returns M
#Overall this is what the function does:The function `func_1` takes a list of tuples `q` and an integer `x` as input. It computes and returns a list `M` containing certain divisors of a value derived from `q` that meet specific conditions related to `x`.

