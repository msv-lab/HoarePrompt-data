#State of the program right berfore the function call: a, b, and c are positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sum of any two of the positive integers a, b, and c is greater than the third integer, otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts three positive integers `a`, `b`, and `c`. It returns `True` if the sum of any two of these integers is greater than the third integer, otherwise it returns `False`.

#State of the program right berfore the function call: n, na, nb, and nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers where 1 ≤ numbers[i] ≤ 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` remains the same, `na` remains the same, `nb` remains the same, `nc` remains the same, `numbers` remains the same, `group_a` contains `na` numbers from `numbers`, `group_b` contains `nb` numbers from `numbers`, `group_c` contains `nc` numbers from `numbers`, `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, and `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with the lists `group_a`, `group_b`, and `group_c`. `group_a` contains `na` numbers from the list `numbers`, `group_b` contains `nb` numbers from the list `numbers`, and `group_c` contains `nc` numbers from the list `numbers`. The sums of the numbers in `group_a`, `group_b`, and `group_c` are `sum_a`, `sum_b`, and `sum_c` respectively, and the condition `func_1(sum_a, sum_b, sum_c)` is true.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts parameters `n`, `na`, `nb`, `nc`, and `numbers`, where `n` is a positive integer, `na`, `nb`, and `nc` are positive integers such that `na + nb + nc = n`, and `numbers` is a list of `n` positive integers. It sorts the list `numbers` in descending order and then distributes the numbers into three groups `group_a`, `group_b`, and `group_c` of sizes `na`, `nb`, and `nc` respectively. The function calculates the sums of the numbers in these groups (`sum_a`, `sum_b`, `sum_c`). If the condition `func_1(sum_a, sum_b, sum_c)` is true, the function returns 'YES' along with the lists `group_a`, `group_b`, and `group_c`. If the condition is not met, the function returns 'NO'. The original list `numbers` remains unchanged in terms of its elements, but it is sorted in descending order within the function.

