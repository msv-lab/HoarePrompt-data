#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns a boolean value indicating whether the sum of any two of the positive integers a, b, and c is greater than the third integer.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`, and returns a boolean value. It returns `True` if the sum of any two of these integers is greater than the third integer, and `False` otherwise. The function does not modify the input variables.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 <= numbers[i] <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n`, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, `numbers` is a list of `n` positive integers sorted in descending order, `group_a` is a list containing the first `na` elements of `numbers`, `group_b` is a list containing the next `nb` elements of `numbers`, `group_c` is a list containing the last `nc` elements of `numbers`, `sum_a` is the sum of the elements in `group_a`, `sum_b` is the sum of the elements in `group_b`, `sum_c` is the sum of the elements in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`, where `group_a` contains the first `na` elements of the sorted list `numbers` in descending order, `group_b` contains the next `nb` elements, and `group_c` contains the last `nc` elements.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and distributes the elements into three groups: `group_a` (first `na` elements), `group_b` (next `nb` elements), and `group_c` (last `nc` elements). It then checks if a condition defined by `func_1` is met for the sums of these groups. If the condition is met, the function returns 'YES' along with the three groups. If the condition is not met, it returns 'NO'.

