#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100,000. For each test case, n, n_a, n_b, n_c are integers such that 3 ≤ n ≤ 200,000, 1 ≤ n_a, n_b, n_c ≤ n-2, and n_a + n_b + n_c = n. Additionally, the list of integers x_1, x_2, ..., x_n has each x_i in the range 1 ≤ x_i ≤ 10^9, and the sum of n across all test cases does not exceed 200,000.
def func_1():
    t = int(input())
    for _ in range(t):
        n, na, nb, nc = map(int, input().split())
        
        x = list(map(int, input().split()))
        
        x.sort(reverse=True)
        
        group_a = x[:na]
        
        group_b = x[na:na + nb]
        
        group_c = x[na + nb:]
        
        sum_a = sum(group_a)
        
        sum_b = sum(group_b)
        
        sum_c = sum(group_c)
        
        if sum_a + sum_b > sum_c and sum_b + sum_c > sum_a and sum_c + sum_a > sum_b:
            print('YES')
            print(' '.join(map(str, group_a)))
            print(' '.join(map(str, group_b)))
            print(' '.join(map(str, group_c)))
        else:
            print('NO')
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 100,000\), `x` is a list of integers sorted in descending order, `na` is an integer, `nb` is an integer, `nc` is an integer, `group_a` is a list consisting of the first `na` elements from `x` and is sorted in descending order, `group_b` is a list consisting of elements from `x` starting at index `na` up to, but not including, index `na + nb`, and these elements are sorted in descending order, `group_c` is a list consisting of the elements from `x` starting at index `na + nb` and is sorted in descending order, `sum_a` is the sum of the elements in `group_a`, `sum_b` is the sum of the elements in `group_b`, `sum_c` is the sum of the elements in `group_c`. After all iterations of the loop, if for every iteration `sum_a + sum_b > sum_c` and `sum_b + sum_c > sum_a` and `sum_c + sum_a > sum_b` are true, then 'YES' is printed and the groups are printed as specified. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( n \) (the size of the list \( x \)), and three integers \( n_a \), \( n_b \), and \( n_c \) which sum up to \( n \). For each test case, it reads a list of integers \( x_1, x_2, \ldots, x_n \) and sorts them in descending order. It then divides the list into three groups: `group_a` of size \( n_a \), `group_b` of size \( n_b \), and `group_c` of size \( n_c \). The function checks if these groups satisfy the triangle inequality conditions: `sum_a + sum_b > sum_c`, `sum_b + sum_c > sum_a`, and `sum_c + sum_a > sum_b`. If the conditions are satisfied for all test cases, the function prints 'YES' followed by the elements of the three groups in separate lines. If any of the conditions fail for any test case, the function prints 'NO'. The function handles up to 100,000 test cases, with each \( n \) ranging from 3 to 200,000, and the sum of all \( n \) values does not exceed 200,000.

