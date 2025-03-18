#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to split into three groups.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the conditions a + b > c, a + c > b, and b + c > a are satisfied, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integers \(a\), \(b\), and \(c\) and returns True if these integers can form the sides of a triangle based on the triangle inequality theorem (i.e., the sum of any two sides must be greater than the third side). Otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ x_i ≤ 10^9 for each x_i in numbers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `sum_a` is the sum of the first `na` elements in `numbers`, `sum_b` is the sum of the next `nb` elements in `numbers`, `sum_c` is the sum of the last `nc` elements in `numbers`, `n` is an integer such that 3 ≤ n ≤ 200,000, `na`, `nb`, and `nc` are integers such that 1 ≤ `na`, `nb`, `nc` ≤ `n`-2 and `na` + `nb` + `nc` = `n`, and `numbers` is a list of `n` positive integers sorted in descending order, and `group_a`, `group_b`, and `group_c` are lists containing the first `na`, next `nb`, and last `nc` elements from `numbers` respectively.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c, where group_a contains the first na elements from numbers, group_b contains the next nb elements from numbers, and group_c contains the last nc elements from numbers.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts four parameters: an integer `n` (between 3 and 200,000), two integers `na` and `nb` (each between 1 and `n-2` and their sum equals `n`), and a list `numbers` of `n` positive integers (each between 1 and 10^9). It sorts the `numbers` list in descending order. Then, it divides the sorted list into three groups based on the values of `na`, `nb`, and `nc` (where `nc` is inferred as `n - na - nb`). If `func_1(sum_a, sum_b, sum_c)` returns true, the function returns 'YES' along with the three groups (`group_a`, `group_b`, `group_c`). Otherwise, it returns 'NO'.

