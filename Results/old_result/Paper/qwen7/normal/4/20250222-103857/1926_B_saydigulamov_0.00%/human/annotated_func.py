#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, with the size of the triangle or square being greater than 1.
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
        
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 100, `a` is an integer representing the number of test cases where 2 ≤ a ≤ 10, `i` is 10, `k` is a list containing the total count of '1' in all input strings `b` where '1' was found for all iterations of the loop, and `b` is the final input string from the user. The first element of `k` is equal to the second element of `k`.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of '0's and '1's. For each test case, it checks if the grid contains exactly one triangle or one square made up of '1's, where the size of the shape is greater than 1. If the counts of '1's in the first two rows are equal, it prints these counts. The function does not return any value but prints the counts if the condition is met.

