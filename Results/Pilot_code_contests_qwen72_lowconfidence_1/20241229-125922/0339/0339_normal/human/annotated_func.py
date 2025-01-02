#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 3 × 10^5, and arr is a list of n integers where each integer is in the range 0 ≤ A_i < 2^60.
def func_1(n, arr):
    sum = 0
    bitcount = [0] * 100
    for num in arr:
        b = reversed(bin(num)[2:])
        
        for i, s in enumerate(b):
            if i != '0':
                bitcount[i] += int(s)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 3 \times 10^5\), `arr` is a list of `n` integers where each integer is in the range \(0 \leq A_i < 2^{60}\), `sum` is 0, `bitcount` is a list of 100 elements where each element at index `i` represents the total count of 1s in the \(i\)-th bit position across all elements in `arr`.
    for (i, b) in enumerate(bitcount):
        sum += b * (n - b) * 2 ** i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 3 \times 10^5\), `arr` is a list of `n` integers where each integer is in the range \(0 \leq A_i < 2^{60}\), `sum` is the sum of \( b_i \times (n - b_i) \times 2^i \) for all \( i \) from 0 to 99, where \( b_i \) is the \( i \)-th element in `bitcount`, `bitcount` is a list of 100 elements where each element at index `i` represents the total count of 1s in the \(i\)-th bit position across all elements in `arr`.
    return sum % (10 ** 9 + 7)
    #The program returns the value of `sum % (10
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `arr` of `n` integers, where each integer is in the range \(0 \leq A_i < 2^{60}\). It calculates the sum of the products of the counts of 1s in each bit position across all elements in `arr` and the corresponding complements, multiplied by the power of 2 for that bit position. The final result is returned modulo \(10^9 + 7\). The function modifies a local variable `sum` and a local list `bitcount` during its execution, but the input parameters `n` and `arr` remain unchanged. The function handles the range of inputs correctly but does not explicitly handle edge cases like empty lists or invalid input ranges, which could lead to unexpected behavior or errors.

#State of the program right berfore the function call: N is an integer such that 2 <= N <= 3 * 10^5, and A_l is a list of N integers where each element A_i satisfies 0 <= A_i < 2^60.
def func_2():
    N = int(input())
    A_l = [int(i) for i in input().split()]
    print(func_1(N, A_l))
#Overall this is what the function does:The function `func_2` reads an integer `N` and a list `A_l` of `N` integers from the standard input. It then calls another function `func_1` with `N` and `A_l` as arguments and prints the result returned by `func_1`. The function does not return any value itself, but its primary purpose is to process the input list `A_l` through `func_1` and output the result. The state of the program after `func_2` concludes is that `N` and `A_l` have been read and processed, and the result of `func_1` has been printed to the standard output.

