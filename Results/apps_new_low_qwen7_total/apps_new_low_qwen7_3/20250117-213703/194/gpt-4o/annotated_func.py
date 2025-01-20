#State of the program right berfore the function call: a, b, c, d are integers such that |a|, |b|, |c|, |d| ≤ 10^9.
def func_1(A):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]

det = a * d - b * c
    if (det == 0) :
        return 0.0
        #The program returns 0.0
    #State of the program after the if block has been executed: a is A[0][0], b is A[0][1], c is A[1][0], d is A[1][1], det is a * d - b * c, and det is not equal to 0
    if (abs(a) >= max(abs(b), abs(c), abs(d))) :
        a_prime = b * c / d if d != 0 else 0

min_norm_value = abs(a - a_prime)
    else :
        if (abs(b) >= max(abs(a), abs(c), abs(d))) :
            b_prime = a * d / c if c != 0 else 0

min_norm_value = abs(b - b_prime)
        else :
            if (abs(c) >= max(abs(a), abs(b), abs(d))) :
                c_prime = a * d / b if b != 0 else 0

min_norm_value = abs(c - c_prime)
            else :
                d_prime = b * c / a if a != 0 else 0

min_norm_value = abs(d - d_prime)
            #State of the program after the if-else block has been executed: `a`, `b`, `c`, `d` are elements of matrix `A`, `det` is the determinant of `A`, which is not equal to 0, and `min_norm_value` is the minimum norm value based on specific conditions. If the absolute value of `c` is greater than or equal to the maximum of the absolute values of `a`, `b`, and `d`, then `c_prime` is `(A[0][0] * A[1][1]) / A[0][1]`, and `min_norm_value` is `abs(A[1][0] - c_prime)`. Otherwise, `d_prime` is `b * c / a` if `a` is not 0, and 0 otherwise, and `min_norm_value` is `abs(d - d_prime)`
        #State of the program after the if-else block has been executed: *`a`, `b`, `c`, `d` are elements of matrix `A`, `det` is the determinant of `A`, which is not equal to 0, and `min_norm_value` is the minimum norm value based on specific conditions. If the absolute value of `b` is greater than or equal to the maximum of the absolute values of `a`, `c`, and `d`, then `min_norm_value` is `abs(b - (a * d / c) if c != 0 else 0)`. Otherwise, `c_prime` is `(A[0][0] * A[1][1]) / A[0][1]` if `c` is not 0, and `d_prime` is `b * c / a` if `a` is not 0, and `min_norm_value` is `abs(A[1][0] - c_prime)` or `abs(d - d_prime)` accordingly.
    #State of the program after the if-else block has been executed: *`a`, `b`, `c`, `d` are elements of matrix `A`, `det` is the determinant of `A` which is not equal to 0, and `min_norm_value` is the minimum norm value based on specific conditions. If the absolute value of `a` is greater than or equal to the maximum of the absolute values of `b`, `c`, and `d`, then `min_norm_value` is `abs(a - (b * c / d))`. Otherwise, if `c` is not 0, `c_prime` is `(A[0][0] * A[1][1]) / A[0][1]`, and `min_norm_value` is `abs(A[1][0] - c_prime)`. If `c` is 0, and `a` is not 0, `d_prime` is `b * c / a`, and `min_norm_value` is `abs(d - d_prime)`.
    return min_norm_value
    #`min_norm_value` is calculated based on specific conditions. If `abs(a)` is greater than or equal to `max(abs(b), abs(c), abs(d))`, then `min_norm_value` is `abs(a - (b * c / d))`. Otherwise, if `c` is not 0, `c_prime` is `(A[0][0] * A[1][1]) / A[0][1]`, and `min_norm_value` is `abs(A[1][0] - c_prime)`. If `c` is 0 and `a` is not 0, `d_prime` is `b * c / a`, and `min_norm_value` is `abs(d - d_prime). The program returns `min_norm_value`
#Overall this is what the function does:The function `func_1` accepts a 2D list `A` containing four integers `[a, b, c, d]`. It calculates the determinant of the matrix formed by these integers and checks if the determinant is zero. If the determinant is zero, the function returns 0.0. If the determinant is non-zero, the function computes several derived values (`a_prime`, `b_prime`, `c_prime`, `d_prime`) based on the maximum absolute value among `a`, `b`, `c`, and `d`. It then determines the minimum norm value (`min_norm_value`) based on specific conditions involving these derived values. The function returns the calculated `min_norm_value`.

#State of the program right berfore the function call: a, b, c, and d are integers such that |a|, |b|, |c|, |d| ≤ 10^9.
def func_2():
    data = input().split()

a, b = int(data[0]), int(data[1])

c, d = int(data[2]), int(data[3])

A = [[a, b], [c, d]]

result = func_1(A)

print(f'{result:.10f}')
#Overall this is what the function does:The function reads four integers from user input, representing the elements of a 2x2 matrix A. It then calls another function `func_1` with this matrix as input. Finally, it prints the result returned by `func_1`, formatted to 10 decimal places. If the input values are outside the range of \( -10^9 \) to \( 10^9 \), the behavior is undefined. No parameters are accepted by this function.

