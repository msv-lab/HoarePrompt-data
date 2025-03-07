#State of the program right berfore the function call: a, b, and c are non-negative integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the non-negative integers (a, b, c) is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three non-negative integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer; otherwise, it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 ≤ numbers[i] ≤ 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: After the loop has executed all iterations:
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the final values of `group_a`, `group_b`, and `group_c` after the loop has executed all iterations. The function `func_1(sum_a, sum_b, sum_c)` evaluated to True, indicating that the conditions specified by `func_1` were met with the sums of `group_a`, `group_b`, and `group_c`.
    else :
        return 'NO'
        #The program returns the string 'NO'.
#Overall this is what the function does:The function `func_2` takes five parameters: `n`, `na`, `nb`, `nc`, and `numbers`. It sorts the `numbers` list in descending order and then distributes the numbers into three groups (`group_a`, `group_b`, `group_c`) based on some internal logic (not shown). After distributing the numbers, it checks if the conditions specified by `func_1` are met using the sums of the numbers in each group. If the conditions are met, the function returns 'YES' along with the final values of `group_a`, `group_b`, and `group_c`. If the conditions are not met, the function returns 'NO'.

