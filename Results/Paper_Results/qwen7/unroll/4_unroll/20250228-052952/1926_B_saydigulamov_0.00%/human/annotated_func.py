#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid.
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
        
    #State: The output will be 'k' which is a list containing the count of '1's in the first two strings provided during the iteration where both counts are equal. If no such iteration exists, nothing is printed.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid represented as a list of strings containing '0's and '1's. For each test case, it counts the number of '1's in the first two strings provided. If these counts are equal, it prints the counts. If no such pair of strings has equal counts, nothing is printed.

