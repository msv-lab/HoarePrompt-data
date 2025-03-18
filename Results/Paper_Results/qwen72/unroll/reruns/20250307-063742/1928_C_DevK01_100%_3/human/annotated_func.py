#State of the program right berfore the function call: q is an integer representing Vasya's position in the line, and x is an integer representing the number Vasya received during the settling, such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: q is an integer representing Vasya's position in the line, x is an integer representing the number Vasya received during the settling, such that 1 <= x < q <= 10^9, M is a list. If w is an integer (i.e., w is a perfect square) and w >= x - 1, then M contains the integer value of the square root of q. Otherwise, M remains empty.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: i = w, M contains all divisors of q that are greater than or equal to x - 1, and their corresponding complementary divisors (q // i) that are also greater than or equal to x - 1.
    return M
    #The program returns M, which contains all divisors of q that are greater than or equal to x - 1, along with their corresponding complementary divisors (q // i) that are also greater than or equal to x - 1.
#Overall this is what the function does:The function `func_1` accepts two integers, `q` and `x`, where `1 <= x < q <= 10^9`. It returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding complementary divisors (i.e., `q // i` where `i` is a divisor) that are also greater than or equal to `x - 1`. If no such divisors exist, the function returns an empty list.

