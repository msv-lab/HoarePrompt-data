#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to be split into three groups.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the conditions a + b > c, a + c > b, and b + c > a are satisfied, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integers \(a\), \(b\), and \(c\) and returns `True` if these integers satisfy the triangle inequality conditions (i.e., \(a + b > c\), \(a + c > b\), and \(b + c > a\)). If any of these conditions are not met, it returns `False`.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n. numbers is a list of n positive integers such that 1 ≤ x_i ≤ 10^9 for each x_i in numbers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: All elements in the `numbers` list have been processed by the function `distribute_number(num)`, and the value of `num` continues to be updated to the next element in the `numbers` list after each call to `distribute_number(num)`. The functions `distribute_number` have been called `n` times, where `n` is the length of the `numbers` list. The variables `group_a`, `group_b`, and `group_c` contain subsets of the original `numbers` list, and `sum_a`, `sum_b`, and `sum_c` represent the sums of the elements in `group_a`, `group_b`, and `group_c`, respectively. The values of `na`, `nb`, and `nc` reflect the sizes of these groups, maintaining the condition `na + nb + nc = n`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: `n` (an integer between 3 and 200,000), `na`, `nb`, and `nc` (integers between 1 and `n-2` such that `na + nb + nc = n`), and a list of `n` positive integers `numbers`. It sorts the `numbers` list in descending order and then distributes the numbers into three groups (`group_a`, `group_b`, and `group_c`) based on the function `distribute_number(num)`. After distributing the numbers, it calculates the sums of the elements in each group (`sum_a`, `sum_b`, and `sum_c`). If the function `func_1(sum_a, sum_b, sum_c)` returns `True`, it returns `'YES'` along with the three groups; otherwise, it returns `'NO'`.

