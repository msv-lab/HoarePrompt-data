#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is represented as a list of n strings, each string containing n characters that are either '0' or '1'. The grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the size of the triangle or square is greater than 1.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `a` is an input integer where 2 ≤ n ≤ 10, and the program prints the count of '1's from the first two inputs if they contain the same number of '1's. Otherwise, it does not print anything.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a grid represented as a list of strings, where each string contains characters '0' or '1'. It counts the number of '1's in each row and stores these counts in a list. If the first two counts are equal, it prints these counts. Otherwise, it does nothing. The function does not return any value but prints the counts of '1's from the first two rows if they match.

