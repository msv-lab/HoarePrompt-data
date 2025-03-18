#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers a, b, and c is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three parameters `a`, `b`, and `c`, which are expected to be positive integers. It returns `True` if the sum of any two of these integers is greater than the third integer; otherwise, it returns `False`. This function is used to determine if the given integers can form the sides of a triangle.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 <= numbers[i] <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n`, `na`, `nb`, and `nc` remain the same positive integers such that `na + nb + nc = n`. `numbers` remains a list of `n` positive integers sorted in descending order. `group_a`, `group_b`, and `group_c` are now lists containing `na`, `nb`, and `nc` elements respectively, where the elements in `group_a` are the largest, followed by `group_b`, and then `group_c`. `sum_a`, `sum_b`, and `sum_c` are now the sums of the elements in `group_a`, `group_b`, and `group_c` respectively.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`, where `group_a` contains the largest `na` elements from the list `numbers`, `group_b` contains the next largest `nb` elements, and `group_c` contains the smallest `nc` elements. The sums of the elements in `group_a`, `group_b`, and `group_c` are `sum_a`, `sum_b`, and `sum_c` respectively, and these sums satisfy the condition `func_1(sum_a, sum_b, sum_c)`.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and then distributes the elements into three groups: `group_a`, `group_b`, and `group_c`, containing `na`, `nb`, and `nc` elements respectively. The function returns 'YES' and the lists `group_a`, `group_b`, and `group_c` if the sums of these groups satisfy the condition `func_1(sum_a, sum_b, sum_c)`. If the condition is not satisfied, it returns 'NO'. After the function concludes, `n`, `na`, `nb`, and `nc` remain unchanged, and `numbers` is sorted in descending order.

