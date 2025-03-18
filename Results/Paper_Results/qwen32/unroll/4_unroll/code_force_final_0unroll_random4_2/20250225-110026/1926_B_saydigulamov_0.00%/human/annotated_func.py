#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 10) representing the size of the grid. The next n lines each contain a string of n characters, where each character is either '0' or '1'. The grid is guaranteed to contain exactly one triangle or exactly one square formed by the '1's, and the size of the shape (number of rows of '1's) is greater than 1.
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
        
    #State: the list `k` containing the counts of '1's in each row where the first two counts are equal.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of '0's and '1's. For each test case, it counts the number of '1's in each row and checks if the first two counts are equal. If they are, it prints the list of counts. The function does not explicitly return a value but prints the counts for test cases where the first two counts of '1's in the rows are equal.

