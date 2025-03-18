#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: After the loop executes all iterations, `t` must be greater than 0, `i` equals `t`, `n` is the last input integer received, `l` is the last list of integers obtained from splitting the input string and converting each element to an integer, `e` is a set containing unique elements from the list `l`, and `m` is the length of the list `l`. If the list `l` contains the integer 1, the output will be 'Bob'. Otherwise, the output will be 'Alice'.
    #
    #This means that after all iterations of the loop have finished, the value of `i` will be equal to the initial value of `t`, and the lists `l` and sets `e` will contain the data from the last iteration. The final output will depend on whether the number 1 is present in the list `l` or not.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of stone piles. For each test case, it reads the number of piles and the number of stones in each pile. It then determines whether the number 1 is present in the list of stones for any pile. If 1 is found, it outputs 'Bob'; otherwise, it outputs 'Alice'. After processing all test cases, the function does not return any value but prints the result for each test case.

