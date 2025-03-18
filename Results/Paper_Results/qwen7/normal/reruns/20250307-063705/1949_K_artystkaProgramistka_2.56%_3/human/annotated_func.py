#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the numbers in the three groups, respectively, such that a + b + c is the sum of a given list of n positive integers, and a, b, and c are non-negative integers satisfying a + b + c = sum_of_x, where sum_of_x is the sum of the integers in the list x_1, x_2, ..., x_n.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c satisfy the triangle inequality conditions (a + b > c, a + c > b, and b + c > a) and False otherwise.
#Overall this is what the function does:The function accepts three parameters a, b, and c, which are positive integers. It returns True if these values satisfy the triangle inequality conditions (a + b > c, a + c > b, and b + c > a). Otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: All elements in the `numbers` list have been processed, `numbers` is now an empty list, and the function `distribute_number(num)` has been called `n` times with each `num` as its argument.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', along with three groups (group_a, group_b, group_c) which were formed during the processing of the numbers list.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: an integer `n` (between 3 and 200,000), and three integers `na`, `nb`, and `nc` (each between 1 and `n-2` such that their sum equals `n`). It also takes a list of `n` positive integers named `numbers`. The function first sorts the `numbers` list in descending order. Then, it distributes the numbers into three groups (`group_a`, `group_b`, `group_c`) by calling the `distribute_number(num)` function for each number in the sorted list. After processing all numbers, it checks the sums of the three groups using the `func_1` function. If the condition in `func_1` is met, the function returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

