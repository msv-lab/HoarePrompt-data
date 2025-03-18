#State of the program right berfore the function call: a, b, and c are integers representing the sums of three groups, and they must satisfy the triangle inequality conditions to form a triangle with positive area.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True, indicating that the sums of the three groups (a, b, and c) satisfy the triangle inequality conditions and can form a triangle with positive area.
#Overall this is what the function does:The function accepts three integer parameters `a`, `b`, and `c`, representing the sums of three groups. It returns `True` if these sums satisfy the triangle inequality conditions, indicating that they can form a triangle with a positive area, and `False` otherwise.

#State of the program right berfore the function call: n is a positive integer, na, nb, nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer, `na`, `nb`, `nc` are positive integers such that `na + nb + nc = n`, and `numbers` is a list of `n` positive integers sorted in descending order; `group_a` contains the first `na` numbers from `numbers`, `group_b` contains the next `nb` numbers from `numbers`, `group_c` contains the last `nc` numbers from `numbers`; `sum_a` is the sum of the first `na` numbers from `numbers`, `sum_b` is the sum of the next `nb` numbers from `numbers`, `sum_c` is the sum of the last `nc` numbers from `numbers`.`
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns ('YES', group_a, group_b, group_c), where group_a contains the first `na` numbers from `numbers`, group_b contains the next `nb` numbers from `numbers`, and group_c contains the last `nc` numbers from `numbers`.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts a positive integer `n`, three positive integers `na`, `nb`, and `nc` such that their sum equals `n`, and a list `numbers` of `n` positive integers. It sorts the list in descending order and attempts to split it into three groups: `group_a` containing the first `na` numbers, `group_b` containing the next `nb` numbers, and `group_c` containing the last `nc` numbers. If a certain condition (checked by `func_1`) is satisfied with the sums of these groups, it returns a tuple ('YES', `group_a`, `group_b`, `group_c`). Otherwise, it returns 'NO'.

