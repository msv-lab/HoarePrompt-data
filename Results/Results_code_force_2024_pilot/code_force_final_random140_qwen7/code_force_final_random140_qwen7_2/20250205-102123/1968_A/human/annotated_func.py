#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: Output State: `num` is a positive integer greater than 0, `i` is equal to `num`, `L1` is a list containing `num` elements, each of which is an integer entered by the user.
    #
    #This means that after the loop has executed all its iterations, `num` will be the final value it was set to during the last iteration, `i` will have reached `num` (since the loop increments `i` from 0 to `num-1`), and `L1` will contain exactly `num` elements, each being an integer input by the user as the loop appended these inputs to the list in each iteration.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: `num` is the final value it was set to during the last iteration, `i` is equal to `num`, `L1` is a list containing `num` elements, each of which is an integer entered by the user, and `j` is `L1[num] + 2`. `res` is a list containing all the values calculated based on the divisors of each element in `L1` from 2 to the respective element + 1.
    print(*res, sep='\n')
    #This is printed: the divisors of each element in L1 from 2 to the respective element + 1, each on a new line
#Overall this is what the function does:The function processes a list of integers entered by the user. For each integer in the list, it calculates and prints the result of dividing the integer by its smallest divisor (other than 1) and then multiplying by one less than that divisor. The function does not return any value.

