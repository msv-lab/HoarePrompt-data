#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers a, b, and c is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer. Otherwise, it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 <= numbers[i] <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n`, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, `numbers` is a list of `n` positive integers where 1 <= `numbers[i]` <= 10^9, sorted in descending order, `group_a`, `group_b`, and `group_c` are lists containing the elements of `numbers` distributed among them, and `sum_a`, `sum_b`, and `sum_c` are the sums of the elements in `group_a`, `group_b`, and `group_c` respectively.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES' along with the lists `group_a`, `group_b`, and `group_c`. Each of these lists contains a portion of the elements from the list `numbers`, which is sorted in descending order. The elements in `group_a`, `group_b`, and `group_c` are distributed such that the sum of the elements in `group_a` is `sum_a`, the sum of the elements in `group_b` is `sum_b`, and the sum of the elements in `group_c` is `sum_c`. The function `func_1(sum_a, sum_b, sum_c)` has returned `True`, indicating that the distribution of elements among the groups is valid.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and then distributes the elements of `numbers` into three groups, `group_a`, `group_b`, and `group_c`, such that the sizes of these groups are `na`, `nb`, and `nc` respectively. The function returns 'YES' and the three groups if the distribution is valid according to an external function `func_1(sum_a, sum_b, sum_c)`, where `sum_a`, `sum_b`, and `sum_c` are the sums of the elements in `group_a`, `group_b`, and `group_c`. If the distribution is not valid, the function returns 'NO'.

