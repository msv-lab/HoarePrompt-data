#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups such that a + b + c is the sum of some set of positive integers, and a, b, and c satisfy the condition a + b + c > 0.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the conditions a + b > c, a + c > b, and b + c > a are satisfied, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integer parameters a, b, and c. It checks whether these values satisfy the triangle inequality theorem (i.e., the sum of any two sides must be greater than the third side). If all conditions a + b > c, a + c > b, and b + c > a are met, the function returns True; otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `sum_a` is 0, `sum_b` is 0, `sum_c` is 0, `numbers` is an empty list, `distribute_number(num)` has been called with an argument `num` three times.
    #
    #This means that after all iterations of the loop have finished, `numbers` will be an empty list because each number from the original list was processed exactly once. The functions `sum_a`, `sum_b`, and `sum_c` remain at 0 as there were no operations modifying these variables within the loop. The function `distribute_number(num)` has been called three times, once for each iteration of the loop.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: `n` (an integer between 3 and 200,000), `na`, `nb`, and `nc` (integers between 1 and `n-2` such that their sum equals `n`), and a list of `n` positive integers called `numbers`. It first sorts the `numbers` list in descending order. Then, it attempts to distribute the numbers into three groups of sizes `na`, `nb`, and `nc` respectively, checking if the sums of the elements in each group can be made equal. If successful, it returns 'YES' along with the sizes of the three groups; otherwise, it returns 'NO'.

