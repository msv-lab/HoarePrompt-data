#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the numbers in three different groups, and the function checks if these sums can form the sides of a triangle with positive area.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c can form the sides of a triangle with positive area, otherwise it returns False.
#Overall this is what the function does:The function checks if three given positive integers can represent the sides of a triangle with a positive area and returns `True` if they can, otherwise it returns `False`.

#State of the program right berfore the function call: n is an integer representing the total number of integers to split, na, nb, nc are integers representing the sizes of the three groups such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is an integer representing the total number of integers to split, `na`, `nb`, `nc` are integers representing the sizes of the three groups such that `na + nb + nc = n`, `numbers` is an empty list, `group_a` contains the first `na` elements of the original `numbers`, `group_b` contains the next `nb` elements of the original `numbers`, `group_c` contains the last `nc` elements of the original `numbers`, `sum_a` is the sum of the elements in `group_a`, `sum_b` is the sum of the elements in `group_b`, `sum_c` is the sum of the elements in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c. Here, group_a contains the first `na` elements of the original `numbers`, group_b contains the next `nb` elements of the original `numbers`, and group_c contains the last `nc` elements of the original `numbers`.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function takes an integer `n`, three integers `na`, `nb`, and `nc` representing the sizes of three groups (where `na + nb + nc = n`), and a list of `n` positive integers. It sorts the list in descending order and distributes the numbers into three groups of sizes `na`, `nb`, and `nc`. If the condition specified in `func_1(sum_a, sum_b, sum_c)` is met, it returns 'YES' along with the three groups; otherwise, it returns 'NO'.

