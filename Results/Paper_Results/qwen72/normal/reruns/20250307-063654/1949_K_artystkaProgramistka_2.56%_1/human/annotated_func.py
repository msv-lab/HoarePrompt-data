#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers a, b, and c is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer. Otherwise, it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that n_a + n_b + n_c = n, and numbers is a list of n positive integers where 1 <= x_i <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer such that `n` ≥ 1, `numbers` is a list of `n` positive integers sorted in descending order, `group_a`, `group_b`, and `group_c` are lists containing elements from `numbers` such that the sum of elements in `group_a` is `sum_a`, the sum of elements in `group_b` is `sum_b`, and the sum of elements in `group_c` is `sum_c`, and the function `distribute_number(num)` has been called for each element in `numbers`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES' along with the lists `group_a`, `group_b`, and `group_c`. These lists contain elements from the original `numbers` list, which is a list of `n` positive integers sorted in descending order. The sum of elements in `group_a` is `sum_a`, the sum of elements in `group_b` is `sum_b`, and the sum of elements in `group_c` is `sum_c`. The condition `func_1(sum_a, sum_b, sum_c)` is true.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_2` accepts five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and attempts to distribute the elements into three groups (`group_a`, `group_b`, and `group_c`). If the sums of the elements in these groups (`sum_a`, `sum_b`, and `sum_c`) satisfy a condition defined by `func_1`, the function returns 'YES' along with the three groups. If the condition is not satisfied, the function returns 'NO'. The `numbers` list is modified to be sorted in descending order, and the three groups are populated with elements from `numbers`.

