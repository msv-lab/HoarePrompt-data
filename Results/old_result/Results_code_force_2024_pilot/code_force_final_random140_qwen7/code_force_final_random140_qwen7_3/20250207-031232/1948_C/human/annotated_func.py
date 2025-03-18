#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>', representing the direction of the arrow in each cell of the respective row of the grid.
def func():
    for j in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('NO')
                break
        else:
            print('YES')
        
    #State: The final output will be 'YES' if for no odd index \(i\) (where \(1 \leq i < n\)) the conditions \(a[i] == '<' \) and \(b[i+1] == '<'\) or \(a[i] == '<' \) and \(b[i-1] == '<'\) are true. Otherwise, the final output will be 'NO'.
#Overall this is what the function does:The function processes two strings of length n, where each character is either '<' or '>', representing the direction of arrows in a grid. It checks for specific conditions at odd indices and prints 'NO' if any condition is met, otherwise it prints 'YES'.

