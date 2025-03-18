#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10) representing the size of an n x n binary grid. Following n is n lines, each containing n characters that are either '0' or '1'. Each grid contains exactly one shape, which is either a triangle or a square, and the shape consists of more than one '1'.
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
        
    #State: i
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an n x n binary grid containing exactly one shape made up of '1's. The shape is either a triangle or a square. The function checks if the number of '1's in the first two rows of the grid are equal and prints the counts if they are.

