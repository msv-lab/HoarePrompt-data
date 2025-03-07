#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of three groups such that a + b + c is the sum of a set of positive integers, and a, b, and c satisfy the condition a + b + c > 0.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the sums a, b, and c satisfy the triangle inequality conditions (a + b > c, a + c > b, and b + c > a)
#Overall this is what the function does:The function accepts three positive integer parameters a, b, and c. It checks whether these values satisfy the triangle inequality conditions (a + b > c, a + c > b, and b + c > a). If the conditions are met, it returns True; otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n. numbers is a list of n positive integers such that 1 ≤ x_i ≤ 10^9 for each x_i in numbers.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: `na` elements are taken from `numbers` and added to `group_a`, `nb` elements are taken from `numbers` and added to `group_b`, `nc` elements are taken from `numbers` and added to `group_c`. The sum of elements in `group_a` is `sum_a`, the sum of elements in `group_b` is `sum_b`, and the sum of elements in `group_c` is `sum_c`. All elements in `numbers` have been distributed, and the original order of elements in `numbers` has been preserved within their respective groups.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` accepts four parameters: `n` (an integer between 3 and 200,000), `na` and `nb` and `nc` (integers between 1 and `n-2` such that their sum equals `n`), and `numbers` (a list of `n` positive integers each between 1 and \(10^9\)). It sorts the `numbers` list in descending order and then distributes the elements into three groups (`group_a`, `group_b`, `group_c`) based on the values of `na`, `nb`, and `nc`. After distribution, it checks if the sums of the elements in these groups satisfy a condition using `func_1`. If the condition is met, it returns `'YES'` along with the three groups; otherwise, it returns `'NO'`.

