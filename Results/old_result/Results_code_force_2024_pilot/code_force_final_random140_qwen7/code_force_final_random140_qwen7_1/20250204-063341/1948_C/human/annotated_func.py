#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; the input consists of t test cases, each test case includes a line with a single integer n, followed by two lines containing strings of length n consisting of characters '<' and/or '>'.
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
        
    #State: Output State: The loop completes all its iterations without encountering any condition that breaks it out. Therefore, the final output is 'YES'.
    #
    #In Natural Language: After the loop has executed all its iterations, the output state is 'YES', indicating that none of the conditions within the loop that would cause it to print 'NO' and break were met. The loop processes each odd index `i` from 1 to `n-2` (since `i` increments by 2 each time), checking the specified conditions. If none of these conditions are satisfied for any `i`, the loop prints 'YES' after completing all iterations.
#Overall this is what the function does:The function processes multiple test cases where each test case includes an integer \( n \) (even and between 2 and \( 2 \times 10^5 \)) and two strings of length \( n \) consisting of characters '<' and/or '>'. For each test case, it checks if there exists an odd index \( i \) from 1 to \( n-2 \) where the character at index \( i \) in the first string matches either the character at index \( i+1 \) or \( i-1 \) in the second string and both are '<'. If such a condition is found, it prints 'NO' and stops processing further. If no such condition is found after checking all possible indices, it prints 'YES'. The function does not return any value but outputs 'YES' or 'NO' for each test case based on the above logic.

