#State of the program right berfore the function call: a, b, and c are positive integers representing the sums of the three groups, and they must satisfy the triangle inequality conditions: a + b > c, a + c > b, and b + c > a.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True
#Overall this is what the function does:The function checks if three given positive integers satisfy the triangle inequality conditions and returns `True` if they do, otherwise it returns `False`.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 200,000, na, nb, nc are positive integers such that na + nb + nc = n, and numbers is a list of n integers where each integer is between 1 and 10^9.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: `group_a` contains the first, fourth, seventh, ..., numbers from `numbers` (depending on the total count and distribution); `group_b` contains the second, fifth, eighth, ..., numbers; `group_c` contains the third, sixth, ninth, ..., numbers; `sum_a` is the sum of the numbers in `group_a`; `sum_b` is the sum of the numbers in `group_b`; `sum_c` is the sum of the numbers in `group_c`.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c. Here, group_a contains the first, fourth, seventh, ..., numbers from the original list 'numbers'; group_b contains the second, fifth, eighth, ..., numbers; and group_c contains the third, sixth, ninth, ..., numbers. The condition `func_1(sum_a, sum_b, sum_c)` is true, where `sum_a` is the sum of the numbers in `group_a`, `sum_b` is the sum of the numbers in `group_b`, and `sum_c` is the sum of the numbers in `group_c`.
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts an integer `n` (3 ≤ n ≤ 200,000), three positive integers `na`, `nb`, and `nc` such that their sum equals `n`, and a list `numbers` of `n` integers where each integer is between 1 and 10^9. It sorts the list in descending order and distributes the numbers into three groups (`group_a`, `group_b`, `group_c`) based on their positions (1st, 4th, 7th, ...; 2nd, 5th, 8th, ...; 3rd, 6th, 9th, ... respectively). It then calculates the sums of these groups. If the condition `func_1(sum_a, sum_b, sum_c)` is true, it returns 'YES' along with the three groups. Otherwise, it returns 'NO'.

