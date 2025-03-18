#State of the program right berfore the function call: a, b, and c are positive integers such that a + b + c = n, where n is the total number of integers to be split into three groups.
def func_1(a, b, c):
    return a + b > c and a + c > b and b + c > a
    #The program returns True if the conditions a + b > c, a + c > b, and b + c > a are satisfied, otherwise it returns False.
#Overall this is what the function does:The function accepts three positive integers a, b, and c. It checks whether these integers can form the sides of a triangle based on the triangle inequality theorem (i.e., the sum of the lengths of any two sides must be greater than the length of the remaining side). If the conditions a + b > c, a + c > b, and b + c > a are all satisfied, the function returns True; otherwise, it returns False.

#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 200,000, na, nb, and nc are integers such that 1 ≤ na, nb, nc ≤ n-2 and na + nb + nc = n, and numbers is a list of n positive integers such that 1 ≤ numbers[i] ≤ 10^9 for all 0 ≤ i < n.
def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
    for num in numbers:
        distribute_number(num)
        
    #State: Output State: All elements from the `numbers` list have been processed, and each element was passed to the `distribute_number` function exactly once. The `numbers` list is now empty. The variables `sum_a`, `sum_b`, and `sum_c` retain their accumulated sums from calling `distribute_number` for each element in the list. The `group_a`, `group_b`, and `group_c` lists contain all the numbers that were originally in the `numbers` list, but distributed among these three groups as per the logic inside the `distribute_number` function.
    if func_1(sum_a, sum_b, sum_c) :
        return 'YES', group_a, group_b, group_c
        #The program returns 'YES', group_a, group_b, group_c
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_2` takes four parameters: `n`, `na`, `nb`, and `nc`, representing the size of a list and the sizes of three subgroups, respectively. It also accepts a list `numbers` containing `n` positive integers. The function sorts the `numbers` list in descending order and then distributes its elements into three groups (`group_a`, `group_b`, `group_c`) based on a custom distribution logic defined within the `distribute_number` function. After processing all elements, it checks if the sums of the three groups are equal using the `func_1` function. If the sums are equal, it returns 'YES' along with the three groups; otherwise, it returns 'NO'.

