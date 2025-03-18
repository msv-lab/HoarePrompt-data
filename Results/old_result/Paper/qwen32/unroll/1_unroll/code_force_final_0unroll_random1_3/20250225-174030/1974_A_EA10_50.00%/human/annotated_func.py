#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers x and y (0 ≤ x, y ≤ 99) where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: 10
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the counts of 1x1 and 2x2 application icons. It calculates and prints the total number of icons required for each test case.

