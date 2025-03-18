#State of the program right berfore the function call: q is an integer representing the position Vasya occupied in the line, and x is an integer representing the number Vasya received during the settling. Both q and x satisfy 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: q is an integer representing Vasya's position in the line, x is an integer representing the number Vasya received during the settling, w is the square root of q, and if w is an integer and greater than or equal to x - 1, then M is [w]. Otherwise, M remains unchanged.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: Output State: q is an integer representing Vasya's position in the line, x is an integer representing the number Vasya received during the settling, w is the square root of q, and M is a list containing integers i and q//i for each i in the range(1, int(w // 1)) such that either i or q//i is greater than or equal to x - 1.
    return M
    #M is a list containing integers i and q//i for each i in the range(1, int(w // 1)) such that either i or q//i is greater than or equal to x - 1.
#Overall this is what the function does:The function accepts two parameters, `q` and `x`, where `q` represents Vasya's position in the line and `x` represents the number Vasya received during the settling. It returns a list `M` containing integers `i` and `q//i` for each `i` in the range from 1 to the integer part of the square root of `q`, such that either `i` or `q//i` is greater than or equal to `x - 1`.

