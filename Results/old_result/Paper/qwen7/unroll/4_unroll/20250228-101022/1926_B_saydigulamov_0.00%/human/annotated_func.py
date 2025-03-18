#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters which are either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid.
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
        
    #State: Output State: The grid contains exactly one triangle or one square that includes all '1's. After the loop executes, if the count of '1's in the first two strings (k[0] and k[1]) are equal, it prints these counts. Otherwise, it does not print anything.
#Overall this is what the function does:The function processes a grid represented as a list of n strings, where n is an integer between 2 and 10. Each string contains n characters that are either '0' or '1', and the grid contains exactly one triangle or one square that includes all the '1's. If the count of '1's in the first two strings of the grid is equal, it prints these counts. Otherwise, it does nothing. The function does not return any value.

