#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to be split into three groups.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if a + b is greater than c, a + c is greater than b, and b + c is greater than a, given that a, b, and c are positive integers such that a + b + c = n.
#Overall this is what the function does:The function accepts three positive integers a, b, and c such that a + b + c = n. It returns True if the sum of any two of these integers is greater than the third one. Otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: All elements from the `numbers` list have been distributed into `group_a`, `group_b`, and `group_c`. The `numbers` list is now empty. `na`, `nb`, and `nc` are integers such that \(1 \leq na, nb, nc \leq 0\) and \(na + nb + nc = 0\). Each of `group_a`, `group_b`, and `group_c` contains exactly one-third of the original elements (rounded down if necessary), and their sums (`sum_a`, `sum_b`, and `sum_c`) reflect the total sum of the elements in each respective group.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts four parameters: an integer `n` (between 3 and 200,000), and three integers `na`, `nb`, and `nc` (each between 1 and `n-2` and summing up to `n`). It also takes a list of `n` positive integers named `numbers`. The function first sorts the `numbers` list in descending order and then distributes the numbers into three groups (`group_a`, `group_b`, `group_c`) based on their size requirements. After distribution, it checks if the sums of the three groups satisfy a certain condition using `func_1`. If the condition is met, the function returns 'YES' along with the three groups; otherwise, it returns 'NO'.

