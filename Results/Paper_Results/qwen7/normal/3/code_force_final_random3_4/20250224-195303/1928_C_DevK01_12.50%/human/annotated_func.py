#State of the program right berfore the function call: q is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), and x is an integer representing the number Vasya received during the settling (1 ≤ x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), and `x` is an integer representing the number Vasya received during the settling (1 ≤ x < q); `M` is a list containing the value of `w`, where `w` is the square root of `q` and is an integer, and `w` is greater than or equal to `x - 1`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: The loop will continue to execute until `i` reaches `w`, which is the integer part of the square root of `q`. For each `i` from 1 to `w`, if `q` is divisible by `i` and `i` is greater than or equal to `x - 1`, or if `q // i` is greater than or equal to `x - 1`, the value of `q // i` will be added to the list `M`. Therefore, `M` will contain all divisors of `q` that are greater than or equal to `x - 1`.
    return M
    #The program returns a list M containing all divisors of q that are greater than or equal to x - 1.
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. `q` represents the position in the line, and `x` represents the number Vasya received during the settling. The function calculates and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`.

