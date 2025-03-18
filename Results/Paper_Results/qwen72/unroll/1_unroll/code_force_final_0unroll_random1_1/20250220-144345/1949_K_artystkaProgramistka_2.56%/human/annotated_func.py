#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers a, b, and c is greater than the third integer. Otherwise, it returns False.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer. Otherwise, it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 <= numbers[i] <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n`, `na`, `nb`, and `nc` remain the same. `numbers` is still a list of `n` positive integers sorted in descending order. `group_a`, `group_b`, and `group_c` are lists containing the first `na`, next `nb`, and last `nc` elements of `numbers`, respectively. `sum_a`, `sum_b`, and `sum_c` are the sums of the elements in `group_a`, `group_b`, and `group_c`, respectively.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`. `group_a` contains the first `na` elements of the sorted list `numbers` in descending order, `group_b` contains the next `nb` elements, and `group_c` contains the last `nc` elements.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_2` accepts five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and then distributes the elements into three groups: `group_a`, `group_b`, and `group_c`, containing the first `na`, next `nb`, and last `nc` elements, respectively. The function calculates the sums of these groups (`sum_a`, `sum_b`, and `sum_c`). If the function `func_1` returns `True` when called with `sum_a`, `sum_b`, and `sum_c`, `func_2` returns 'YES' along with the three groups. Otherwise, it returns 'NO'. The original parameters `n`, `na`, `nb`, and `nc` remain unchanged, and `numbers` is sorted in descending order.

