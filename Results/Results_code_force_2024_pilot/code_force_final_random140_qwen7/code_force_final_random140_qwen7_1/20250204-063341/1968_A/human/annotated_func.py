#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 1000\), `x` is an integer such that \(2 \leq x \leq 1000\), `num` is an input integer, `L1` is a list containing `num` elements, each being an integer entered by the user, `res` is an empty list, `i` is equal to `num`, and `num` must be greater than 0.
    #
    #This means that after the loop has executed all its iterations, `L1` will contain exactly `num` elements, each of which is an integer input by the user. The variable `i` will be equal to `num` because the loop increments `i` until it reaches `num`. The variables `t` and `x` remain unchanged as they were not affected by the loop. The list `res` remains empty since no operations were performed on it within the loop.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 1000\), `x` is an integer such that \(2 \leq x \leq 1000\), `num` must be greater than 0, `i` is equal to `num`, `L1` contains exactly `num` elements, each of which is an integer input by the user, and `res` is a list containing the results of the operations performed within the loop for each iteration.
    print(*res, sep='\n')
    #This is printed: the elements of res, each on a new line
#Overall this is what the function does:The function processes a series of integers entered by the user. For each integer, it finds the largest divisor (other than itself) and multiplies it by one less than itself, then stores these results in a list. Finally, it prints each result on a new line.

