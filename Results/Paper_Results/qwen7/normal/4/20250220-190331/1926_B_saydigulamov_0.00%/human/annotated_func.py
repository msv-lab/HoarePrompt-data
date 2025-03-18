#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of t test cases, each test case starts with an integer n followed by n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid.
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
        
    #State: After all iterations, `a` is the initial number of test cases, `i` takes on the value of the total number of test cases processed (which is equal to `a`), `b` is the concatenated string of all input strings from each test case, and `k` is a list where the first element is the total count of '1's in all test cases, and the second element is also the total count of '1's in all test cases. Since the condition `if k[0] == k[1]: print(k)` always holds true given the problem constraints (both elements of `k` will be equal as they represent the same total count), `k` will be printed after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of '0's and '1's. For each grid, it counts the number of '1's and checks if the '1's form a square or a triangle. If the counts match, it prints the counts. The function does not return any value but prints the counts of '1's if they form a square or a triangle.

