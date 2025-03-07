#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5, and a is a string of length n consisting of characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: Output State: `i` is 'F', `p` is 'ABCDEF', `ans` is the total adjustment made during each iteration based on the condition `if hmp[i] < m`, `t` is the initial input integer between 1 and 1000, `n` is the input integer, `m` is the input integer, `s` is the input string, and `hmp` is a Counter object counting the occurrences of each character in the string `s` including 'F', 'A', 'B', 'C', 'D', and 'E'.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `i` will be set to 'F', indicating that it has iterated through all the characters in the string `p` ('ABCDEF'). The variable `ans` will hold the total adjustment made during each iteration based on the condition `if hmp[i] < m`, reflecting how many times `m` exceeded the count of each character in the string `s` that was less than `m`. The variable `p` remains 'ABCDEF', and all other variables (`t`, `n`, `m`, `s`, `hmp`) retain their initial or final states from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( t \) (indicating the number of test cases), two integers \( n \) and \( m \), and a string \( s \) of length \( n \) containing characters from 'A' to 'G'. For each test case, the function calculates and prints the total adjustment needed based on the condition that if the count of any character in \( s \) is less than \( m \), the adjustment is \( m \) minus the count of that character. The final output is the total adjustment for each test case.

