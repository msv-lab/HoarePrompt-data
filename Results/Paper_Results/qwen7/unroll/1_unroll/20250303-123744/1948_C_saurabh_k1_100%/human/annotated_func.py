#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>', representing the direction of the arrow in each cell of the respective row of the grid.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: Output State: The output state will consist of a series of 'Yes' or 'No' responses printed to the console. For each value of `n`, the program checks pairs of characters from strings `a` and `b`. If it finds a pair where both characters are '<' at specific positions (either directly adjacent or one position apart), it prints 'No' and stops further checks for that `n`. Otherwise, after completing the checks for all relevant positions, it prints 'Yes'. The exact sequence of 'Yes' and 'No' depends on the input values provided for `a` and `b` for each `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of length n, where each character is either '<' or '>'. For each test case, it checks pairs of characters from the two strings at specific positions. If it finds a pair where both characters are '<' at certain positions (either directly adjacent or one position apart), it prints 'No' and stops further checks. Otherwise, after completing the checks for all relevant positions, it prints 'Yes'. The function does not return any value but prints a series of 'Yes' or 'No' responses based on the input strings for each test case.

