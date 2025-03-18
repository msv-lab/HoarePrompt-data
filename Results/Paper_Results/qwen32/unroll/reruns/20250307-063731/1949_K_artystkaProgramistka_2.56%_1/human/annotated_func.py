#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups of numbers, and the function checks if these sums can form the sides of a triangle with positive area.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c can form the sides of a triangle with positive area, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integer parameters representing the sums of three groups of numbers. It returns `True` if these sums can form the sides of a triangle with a positive area, otherwise it returns `False`.

#State of the program right berfore the function call: n is a positive integer representing the total number of integers, na, nb, and nc are positive integers representing the sizes of the three groups such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `group_a` contains `na` numbers, `group_b` contains `nb` numbers, `group_c` contains `nc` numbers; `sum_a` is the sum of numbers in `group_a`, `sum_b` is the sum of numbers in `group_b`, `sum_c` is the sum of numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a which contains `na` numbers, group_b which contains `nb` numbers, and group_c which contains `nc` numbers.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts a positive integer `n`, three positive integers `na`, `nb`, and `nc` representing the sizes of three groups such that `na + nb + nc = n`, and a list `numbers` of `n` positive integers. It attempts to partition the list into three groups of sizes `na`, `nb`, and `nc` respectively. If successful, it returns 'YES' along with the three groups; otherwise, it returns 'NO'.

