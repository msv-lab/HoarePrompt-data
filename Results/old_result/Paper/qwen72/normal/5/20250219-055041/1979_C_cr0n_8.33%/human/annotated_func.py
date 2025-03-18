#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each element in cases is a list containing two elements: an integer n (1 ≤ n ≤ 50) representing the number of outcomes, and a list of n integers k_1, k_2, ..., k_n (2 ≤ k_i ≤ 20) representing the multipliers for the amount of coins if the i-th outcome is winning.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `cases` is a list of test cases, `N` is an input integer, `vals` is a list of integers, `prod` is now equal to the product of all elements in `vals`, `r` is the last element of `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns nothing.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `cases` is a list of test cases, `N` is an input integer, `vals` is a list of integers, `prod` is now equal to the product of all elements in `vals`, `r` is the last element of `vals`, `vprod` is a list where each element is the product of all elements in `vals` except the corresponding element in `vals`, and `den` is equal to `prod` - the sum of all elements in `vprod`. Additionally, `den` is greater than 0.
    print(' '.join([str(x) for x in vprod]))
    #This is printed: [vprod elements separated by spaces] (where each element in vprod is the product of all elements in vals except the corresponding element in vals)
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, followed by a list of `N` integers. It calculates the product of all integers in the list (`prod`), and then computes a new list (`vprod`) where each element is the product of all integers in the list except the corresponding element. It also calculates a denominator (`den`) as the difference between `prod` and the sum of all elements in `vprod`. If `den` is less than or equal to 0, the function prints `-1` and returns. Otherwise, it prints the elements of `vprod` separated by spaces. The function does not accept any parameters and returns nothing.

