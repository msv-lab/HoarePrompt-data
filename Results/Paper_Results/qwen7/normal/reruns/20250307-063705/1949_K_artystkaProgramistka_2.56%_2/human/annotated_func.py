#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to split into three groups, and 1 <= a, b, c <= n-2.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the values of a, b, and c satisfy the triangle inequality theorem, meaning a + b > c, a + c > b, and b + c > a.
#Overall this is what the function does:The function accepts three parameters \(a\), \(b\), and \(c\), which are positive integers such that \(a + b + c = n\) (where \(n\) is the total number of integers to split into three groups) and \(1 \leq a, b, c \leq n-2\). It returns True if these values satisfy the triangle inequality theorem, meaning \(a + b > c\), \(a + c > b\), and \(b + c > a\).

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `sum_a` is 0, `sum_b` is 0, `sum_c` is 0, `n` is an integer such that 3 ≤ n ≤ 200,000, `na`, `nb`, and `nc` are integers such that 1 ≤ `na`, `nb`, `nc` ≤ `n-2` and `na + nb + nc = n`, `numbers` is a list of `n-2` positive integers such that 1 ≤ `numbers[i]` ≤ 10^9 for all 0 ≤ i < `n-2` and is sorted in descending order, `group_a`, `group_b`, and `group_c` are non-empty lists containing the first three elements of `numbers`, and `distribute_number(num)` has been called for each of the first three elements in the `numbers` list.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c, where group_a, group_b, and group_c are non-empty lists containing the first three elements of the sorted list 'numbers' in descending order.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts four parameters: n (an integer between 3 and 200,000), na, nb, and nc (integers between 1 and n-2 such that na + nb + nc = n), and a list of n positive integers named numbers. It sorts the numbers in descending order, then checks if it can divide the first three elements of the sorted list into three non-empty groups. If it can, it returns 'YES' along with these three groups; otherwise, it returns 'NO'.

