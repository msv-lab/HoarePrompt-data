#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to split into three groups, and 1 ≤ a, b, c ≤ n-2.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if a + b > c, a + c > b, and b + c > a are all true, given that a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to split into three groups, and 1 ≤ a, b, c ≤ n-2.
#Overall this is what the function does:The function accepts three parameters \(a\), \(b\), and \(c\), which are positive integers such that \(a + b + c = n\), where \(n\) is the total number of integers to split into three groups, and \(1 \leq a, b, c \leq n-2\). It returns True if the conditions \(a + b > c\), \(a + c > b\), and \(b + c > a\) are all satisfied.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `sum_a`, `sum_b`, `sum_c` are the sums of the elements in `group_a`, `group_b`, `group_c` respectively; `group_a`, `group_b`, `group_c` are lists containing the first `na`, `nb`, `nc` elements from the `numbers` list in their original order; `numbers` is an empty list since all elements have been distributed; `n`, `na`, `nb`, `nc` retain their initial values; `sum_a`, `sum_b`, `sum_c` are the sums of the largest `na`, `nb`, `nc` elements from the original `numbers` list.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: `n`, `na`, `nb`, and `nc`, representing the total number of elements, and the sizes of three groups, respectively. It also takes a list `numbers` containing `n` positive integers. The function sorts the `numbers` list in descending order and then distributes the elements into three groups (`group_a`, `group_b`, `group_c`) based on their original order. After distribution, it calculates the sum of elements in each group. If the function `func_1` returns true when given the sums of these groups, it returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

