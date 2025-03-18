#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the numbers in three different groups, and the function checks if these sums can form the sides of a triangle with positive area.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c can form the sides of a triangle with positive area, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c`, representing sums of numbers in three different groups. It returns `True` if these sums can form the sides of a triangle with a positive area; otherwise, it returns `False`.

#State of the program right berfore the function call: n is an integer representing the total number of integers, na, nb, and nc are integers representing the sizes of the three groups such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is an integer representing the total number of integers, `na`, `nb`, and `nc` are integers representing the sizes of the three groups such that `na + nb + nc = n`, and `numbers` is a list of `n` positive integers sorted in descending order; `group_a` is a list containing the first `na` numbers from `numbers`, `group_b` is a list containing the next `nb` numbers from `numbers`, and `group_c` is a list containing the last `nc` numbers from `numbers`; `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c. Here, 'YES' is a string, group_a is a list containing the first `na` numbers from `numbers`, group_b is a list containing the next `nb` numbers from `numbers`, and group_c is a list containing the last `nc` numbers from `numbers`. The sum of the numbers in group_a, group_b, and group_c satisfy the condition `func_1(sum_a, sum_b, sum_c)` which is true.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` takes an integer `n`, three integers `na`, `nb`, and `nc` representing the sizes of three groups, and a list `numbers` of `n` positive integers. It sorts the list in descending order and attempts to split it into three groups of sizes `na`, `nb`, and `nc`. If the sums of these groups satisfy a condition defined by `func_1`, it returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

