#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups of numbers, and they must satisfy the triangle inequality conditions: a + b > c, a + c > b, and b + c > a.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True
#Overall this is what the function does:The function checks if three given positive integers `a`, `b`, and `c` satisfy the triangle inequality conditions. It returns `True` if all conditions (a + b > c, a + c > b, and b + c > a) are met, indicating that the numbers can form the sides of a triangle.

#State of the program right berfore the function call: n is a positive integer, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, `numbers` is a list of `n` positive integers sorted in descending order, `group_a` is a list containing `na` numbers, `group_b` is a list containing `nb` numbers, `group_c` is a list containing `nc` numbers, `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function takes a positive integer `n` and three other positive integers `na`, `nb`, and `nc` such that their sum equals `n`. It also takes a list `numbers` of `n` positive integers. The function attempts to partition the list `numbers` into three groups of sizes `na`, `nb`, and `nc` respectively. If such a partition is possible and the condition checked by `func_1` is satisfied, it returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

