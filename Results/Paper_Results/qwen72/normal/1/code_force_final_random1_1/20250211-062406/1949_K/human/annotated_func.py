#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers (a, b, and c) is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer; otherwise, it returns `False`. This function checks whether the given integers can form the sides of a triangle.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 ≤ numbers[i] ≤ 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: After all iterations of the loop, `n`, `na`, `nb`, and `nc` remain positive integers such that `na + nb + nc = n`. `numbers` is an empty list. `group_a`, `group_b`, and `group_c` contain the elements from the original `numbers` list distributed according to the `distribute_number` function. `sum_a`, `sum_b`, and `sum_c` are the sums of the elements in `group_a`, `group_b`, and `group_c`, respectively.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`. These lists contain the elements from the original `numbers` list distributed according to the `distribute_number` function, ensuring that the sums of the elements in `group_a`, `group_b`, and `group_c` satisfy the condition that `func_1(sum_a, sum_b, sum_c)` returns `True`.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_2` takes five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and then distributes the elements into three groups (`group_a`, `group_b`, and `group_c`) based on a distribution logic defined by the `distribute_number` function. After distributing the numbers, it checks if the sums of the elements in these groups (`sum_a`, `sum_b`, and `sum_c`) satisfy a condition defined by `func_1`. If the condition is met, the function returns 'YES' along with the three groups. If the condition is not met, it returns 'NO'. The original `numbers` list is emptied during the process.

