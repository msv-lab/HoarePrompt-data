#State of the program right berfore the function call: q is an integer representing the position in the line (1 <= x < n <= 10^9), and x is an integer representing the number Vasya received during the settling (1 <= x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 <= x < n <= 10^9), `x` is an integer representing the number Vasya received during the settling (1 <= x < q), `M` is a list containing one element which is the square root of `q` (denoted as `w`), and `w` is the square root of `q` and is an integer. If `w` is an integer and greater than or equal to `x - 1`, then `w` remains unchanged. Otherwise, no change occurs in the list `M`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: The list `M` contains all divisors of `q` that are greater than or equal to `x - 1`, and `w` is the integer square root of `q`.
    return M
    #The program returns the list M which contains all divisors of q that are greater than or equal to x - 1
#Overall this is what the function does:The function accepts two parameters, q and x. q is an integer representing the position in the line, and x is an integer representing the number Vasya received during the settling. The function calculates all divisors of q that are greater than or equal to x - 1 and returns them in a list M. If the square root of q (denoted as w) is an integer and greater than or equal to x - 1, it is added to the list M. The function then iterates through numbers from 1 to the integer part of the square root of q, checking if they are divisors of q and if they are greater than or equal to x - 1, adding them to the list M. Similarly, it checks their corresponding divisors (q divided by the current number) and adds those to the list M if they meet the criteria.

