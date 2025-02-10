#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and x is a positive integer such that 2 <= x <= 1000 for each test case.
def func():
    num = int(input('Enter number of entries- '))
    L1 = []
    res = []
    for i in range(num):
        L1.append(int(input('Enter entry no.' + str(i + 1) + '- ')))
        
    #State: `t` is a positive integer such that 1 <= t <= 1000, `x` is a positive integer such that 2 <= x <= 1000 for each test case, `num` is a positive integer, `L1` is a list containing `num` integers, `res` is an empty list, `i` is `num - 1`.
    for i in range(num):
        for j in range(2, L1[i] + 1):
            if L1[i] % j == 0:
                res.append(L1[i] // j * (j - 1))
                break
        
    #State: `t` is a positive integer such that 1 <= t <= 1000, `x` is a positive integer such that 2 <= x <= 1000 for each test case, `num` is a positive integer, `L1` is a list containing `num` integers, `i` is `num - 1`, `res` is a list. For each integer `L1[i]` (where `i` ranges from 0 to `num - 1`), if `L1[i]` is divisible by any integer `j` in the range [2, `L1[i]`], then `res` contains the value `L1[i] // j * (j - 1)` for the smallest such `j`. If `L1[i]` is a prime number, `res` remains unchanged from its previous state.
    print(*res, sep='\n')
    #This is printed: 5
    #10
    #14
#Overall this is what the function does:The function `func` does not accept any parameters. It prompts the user to enter the number of entries, followed by the actual entries. For each entry, it calculates a specific value based on the smallest divisor greater than 1 and appends this value to a result list. The function then prints each value in the result list on a new line. The final state of the program includes the printed values, and the function does not return any value.

