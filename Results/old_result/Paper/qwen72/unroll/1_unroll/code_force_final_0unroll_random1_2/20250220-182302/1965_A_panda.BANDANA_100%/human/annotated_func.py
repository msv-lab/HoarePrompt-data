#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains integers representing the number of stones in each pile for a test case. Each test case list should have a length n (1 ≤ n ≤ 2·10^5) and each integer a_i in the list should satisfy 1 ≤ a_i ≤ 10^9. The sum of n over all test cases should not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The loop will print 'Alice' or 'Bob' for each test case based on the conditions specified in the loop. The variables `i`, `n`, `l`, `lis`, and `test` will be in their final states after the loop completes, but their specific values are not retained after each iteration. The variable `t` will be unchanged as it is only used to determine the number of iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the number of piles, followed by a list of integers representing the number of stones in each pile. The function then determines and prints 'Alice' or 'Bob' for each test case based on the following rules: If the list of unique stone counts does not contain 1 or has only one unique value, 'Alice' is printed. Otherwise, if there is a gap greater than 1 between any two consecutive unique stone counts, 'Bob' or 'Alice' is printed based on the parity of the index of the gap. If no such gap exists, 'Alice' or 'Bob' is printed based on the parity of the length of the unique stone counts. The function does not return any value.

