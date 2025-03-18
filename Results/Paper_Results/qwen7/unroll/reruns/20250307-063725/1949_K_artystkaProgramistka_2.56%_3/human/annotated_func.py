#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to split into three groups.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if a + b > c, a + c > b, and b + c > a are all true, given that a, b, and c are positive integers such that a + b + c = n.
#Overall this is what the function does:The function accepts three positive integers a, b, and c such that a + b + c = n. It returns True if the conditions a + b > c, a + c > b, and b + c > a are all satisfied. If any of these conditions are not met, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `sum_a`, `sum_b`, and `sum_c` are the sums of the elements in `group_a`, `group_b`, and `group_c` respectively; `group_a`, `group_b`, and `group_c` are lists containing `na`, `nb`, and `nc` elements from the `numbers` list, selected such that each element in `numbers` is distributed exactly once among the three groups; `n`, `na`, `nb`, `nc`, and `sums` (assuming `sums` is not affected by the loop) retain their initial values; `numbers` is an empty list since all elements have been distributed.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: `n`, `na`, `nb`, and `nc`, representing an integer range and three group sizes, and a list of integers named `numbers`. It sorts the `numbers` list in descending order and then distributes the elements into three groups (`group_a`, `group_b`, `group_c`) based on the specified sizes. After distribution, it checks if the sums of the elements in these three groups are equal using `func_1`. If the sums are equal, it returns `'YES'` along with the three groups; otherwise, it returns `'NO'`.

