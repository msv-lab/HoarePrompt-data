#State of the program right berfore the function call: a, b, and c are non-negative integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the non-negative integers (a, b, c) is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three non-negative integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer. Otherwise, it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 ≤ numbers[i] ≤ 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: After all iterations of the loop, `n`, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, `numbers` is a list of `n` positive integers where 1 ≤ `numbers[i]` ≤ 10^9, sorted in descending order, `group_a` contains the first `na` elements of `numbers`, `group_b` contains the next `nb` elements of `numbers`, `group_c` contains the last `nc` elements of `numbers`, `sum_a` is the sum of the elements in `group_a`, `sum_b` is the sum of the elements in `group_b`, and `sum_c` is the sum of the elements in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`. `group_a` contains the first `na` elements of the sorted list `numbers`, `group_b` contains the next `nb` elements, and `group_c` contains the last `nc` elements. The sums of the elements in `group_a`, `group_b`, and `group_c` are `sum_a`, `sum_b`, and `sum_c` respectively, and the function `func_1(sum_a, sum_b, sum_c)` returns `True`.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_2` takes five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the list `numbers` in descending order and then distributes the elements into three groups: `group_a`, `group_b`, and `group_c`, containing the first `na`, the next `nb`, and the last `nc` elements of the sorted list, respectively. The function calculates the sums of the elements in each group (`sum_a`, `sum_b`, and `sum_c`). If the function `func_1(sum_a, sum_b, sum_c)` returns `True`, the function returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

