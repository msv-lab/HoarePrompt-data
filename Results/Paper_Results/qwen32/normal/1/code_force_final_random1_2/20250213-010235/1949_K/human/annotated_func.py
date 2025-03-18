#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the numbers in three different groups, and the function checks if these sums can form the sides of a triangle with positive area.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c can form the sides of a triangle with positive area, otherwise it returns False.
#Overall this is what the function does:The function checks if three given positive integers can represent the side lengths of a triangle with a positive area and returns `True` if they can, otherwise it returns `False`.

#State of the program right berfore the function call: n is a positive integer representing the total number of integers, na, nb, and nc are positive integers representing the sizes of the three groups such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, `numbers` is a list of `n` positive integers sorted in descending order, `group_a` contains the first `na` elements of `numbers`, `group_b` contains the next `nb` elements of `numbers`, `group_c` contains the last `nc` elements of `numbers`, `sum_a` is the sum of the first `na` elements of `numbers`, `sum_b` is the sum of the next `nb` elements of `numbers`, `sum_c` is the sum of the last `nc` elements of `numbers`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns ('YES', group_a, group_b, group_c) where group_a contains the first `na` elements of `numbers`, group_b contains the next `nb` elements of `numbers`, and group_c contains the last `nc` elements of `numbers`.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function takes a positive integer `n`, three positive integers `na`, `nb`, and `nc` such that their sum equals `n`, and a list of `n` positive integers. It sorts the list in descending order and attempts to distribute the numbers into three groups of sizes `na`, `nb`, and `nc`. If the condition specified by `func_1(sum_a, sum_b, sum_c)` is met, it returns a tuple containing 'YES' and the three groups; otherwise, it returns 'NO'.

