#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups, and they satisfy the condition a + b + c = sum(a_list), where a_list is a list of n positive integers.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums of any two groups (a, b, or c) are greater than the sum of the third group, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integer parameters a, b, and c. It checks whether the sum of any two of these integers is greater than the third one. If this condition is met for any pair, the function returns True; otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ x_i ≤ 10^9 for each x_i in numbers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `numbers` is a list of n sorted positive integers in descending order; `group_a` is a list containing all the numbers from the original `numbers` list; `group_b` is an empty list; `group_c` is an empty list; `sum_a` is the sum of all the numbers in the original `numbers` list; `sum_b` is 0; `sum_c` is 0.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a which contains all the numbers from the original numbers list, group_b which is an empty list, and group_c which is also an empty list.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts four parameters: an integer `n` (between 3 and 200,000), and three integers `na`, `nb`, and `nc` (each between 1 and `n-2` such that `na + nb + nc = n`). It also takes a list `numbers` of `n` positive integers (each between 1 and 10^9). The function sorts the `numbers` list in descending order. It then checks if it's possible to partition the `numbers` list into three groups (`group_a`, `group_b`, and `group_c`) based on certain conditions using `func_1`. If successful, it returns 'YES' along with `group_a` (which contains all elements from the original `numbers` list), an empty `group_b`, and an empty `group_c`. If not possible, it returns 'NO'.

