#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups of numbers, and they must satisfy the triangle inequality conditions: a + b > c, a + c > b, and b + c > a.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True
#Overall this is what the function does:The function checks if three given positive integers `a`, `b`, and `c` satisfy the triangle inequality conditions. If they do, it returns `True`; otherwise, it returns `False`.

#State of the program right berfore the function call: n is a positive integer, na, nb, nc are positive integers such that na + nb + nc = n, and numbers is a list of n positive integers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `n` is a positive integer, `na`, `nb`, `nc` are positive integers such that `na + nb + nc = 0`, and `numbers` is an empty list; `group_a`, `group_b`, and `group_c` are lists containing all the numbers from the original `numbers` list distributed to keep the sums as balanced as possible; `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns ('YES', group_a, group_b, group_c) where group_a, group_b, and group_c are lists containing all the numbers from the original numbers list distributed to keep the sums as balanced as possible, and the function func_1(sum_a, sum_b, sum_c) evaluates to True for the current values of sum_a, sum_b, and sum_c.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function takes a positive integer `n` and three other positive integers `na`, `nb`, and `nc` such that their sum equals `n`, along with a list `numbers` of `n` positive integers. It attempts to distribute the numbers into three groups `group_a`, `group_b`, and `group_c` of sizes `na`, `nb`, and `nc` respectively, aiming to balance the sums of the numbers in each group. If the distribution results in sums that satisfy a condition checked by `func_1`, it returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

