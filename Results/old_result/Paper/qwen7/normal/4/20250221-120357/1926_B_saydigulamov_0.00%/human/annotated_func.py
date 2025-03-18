#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is represented as a list of n strings, each string containing n characters that are either '0' or '1'. It is guaranteed that the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the size of the triangle or square is greater than 1.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `a` is the final input integer which is one more than the last input integer provided during the loop executions, `i` is the total number of iterations (which is equal to the sum of all integers input during the loop executions), `k` is a list containing the cumulative count of '1's from all input strings `b` provided during the loop executions. The value of `b` is the last input string provided by the user, and the postcondition remains unchanged as long as the first element of `k` is equal to the second element of `k`. However, since there is no else part, the postcondition does not change regardless of the if condition.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will still be between 1 and 100, `a` will be the sum of all integers input during the loop, `i` will be the total number of iterations, `k` will contain the cumulative count of '1's from all input strings, and `b` will be the last input string. The if condition does not alter the state of `k` or `b` unless the first and second elements of `k` are equal, but even then, the state does not change due to the lack of an else part.
#Overall this is what the function does:The function processes a grid represented as a list of n strings, where each string contains n characters ('0' or '1'). It counts the number of '1's in each row and stores these counts in a list. If the first two counts in the list are equal, it prints the list. The function does not return any value but prints the list of counts if the specified condition is met.

