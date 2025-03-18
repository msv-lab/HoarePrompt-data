#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of n characters consisting only of '.', '@', and '*', where the first character is always '.', indicating an empty starting cell.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: After all iterations of the loop have finished, `s` will be the total count of '@' characters across all strings `b` provided during the loop's iterations, `i` will be equal to the final value of `a` (which is the number of iterations the loop executed), `a` will remain the same as its initial value, `d` will be the last input integer provided, and `b` will be the last non-empty string provided.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it counts the number of '@' characters in a string of length up to 50, which consists of '.', '@', and '*' characters. It prints the count for each case and maintains a total count of '@' characters across all cases. After processing all cases, it outputs the total count of '@' characters. The function does not return any value but prints the results directly.

