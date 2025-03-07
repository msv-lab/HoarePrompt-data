#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the three groups, and they must satisfy the triangle inequality conditions: a + b > c, a + c > b, and b + c > a.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True
#Overall this is what the function does:The function checks if three given positive integers satisfy the triangle inequality conditions and returns True if they do.

#State of the program right berfore the function call: n is a positive integer such that 3 <= n <= 200,000, na, nb, nc are positive integers such that 1 <= na, nb, nc <= n-2, and na + nb + nc = n. numbers is a list of n positive integers where each integer x_i satisfies 1 <= x_i <= 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `group_a` contains the `na` largest numbers from `numbers`, `group_b` contains the next `nb` largest numbers, `group_c` contains the remaining `nc` numbers, `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, and `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a which contains the na largest numbers from numbers, group_b which contains the next nb largest numbers, and group_c which contains the remaining nc numbers.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` (3 ≤ n ≤ 200,000), three positive integers `na`, `nb`, and `nc` (each between 1 and n-2, and their sum equals `n`), and a list of `n` positive integers `numbers` (each between 1 and 10^9). It sorts the list `numbers` in descending order and attempts to distribute the numbers into three groups: `group_a` containing the `na` largest numbers, `group_b` containing the next `nb` largest numbers, and `group_c` containing the remaining `nc` numbers. It then checks if a condition (determined by `func_1`) is met with the sums of these groups. If the condition is met, it returns 'YES' along with the three groups. If not, it returns 'NO'.

