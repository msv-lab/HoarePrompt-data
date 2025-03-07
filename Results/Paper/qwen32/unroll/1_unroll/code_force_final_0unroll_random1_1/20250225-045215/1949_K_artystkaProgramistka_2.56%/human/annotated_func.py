#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups of numbers, and they must satisfy the triangle inequality conditions: a + b > c, a + c > b, and b + c > a.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True
#Overall this is what the function does:The function checks if three given positive integers `a`, `b`, and `c` can form the sides of a triangle by verifying the triangle inequality conditions. It returns `True` if the conditions are satisfied, otherwise it returns `False`.

#State of the program right berfore the function call: n is a positive integer, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, and `numbers` is a list of `n` positive integers sorted in descending order; `group_a` is a list containing `na` numbers from `numbers`, `group_b` is a list containing `nb` numbers from `numbers`, and `group_c` is a list containing `nc` numbers from `numbers`; `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, and `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c where group_a contains na numbers, group_b contains nb numbers, and group_c contains nc numbers from the list 'numbers' sorted in descending order, and the condition func_1(sum_a, sum_b, sum_c) is true.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts a positive integer `n`, three positive integers `na`, `nb`, and `nc` such that their sum equals `n`, and a list of `n` positive integers `numbers`. It returns 'YES' along with three groups `group_a`, `group_b`, and `group_c` if it is possible to partition the numbers into these groups such that `group_a` contains `na` numbers, `group_b` contains `nb` numbers, and `group_c` contains `nc` numbers, and the condition `func_1(sum_a, sum_b, sum_c)` is true. Otherwise, it returns 'NO'.

