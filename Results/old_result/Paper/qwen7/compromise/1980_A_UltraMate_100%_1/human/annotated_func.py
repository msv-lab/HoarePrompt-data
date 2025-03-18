#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5, and a is a string of n characters where each character is one of 'A', 'B', 'C', 'D', 'E', 'F', or 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: Output State: After the loop executes all the iterations, the variable `i` will be 'A', as the loop processes each character in the order they appear in 'ABCDEFG'. The variable `ans` will be the sum of all increments made during the loop iterations. Specifically, for each character in 'ABCDEFG' that is not found in `hmp`, `ans` will be increased by `m`. If a character from 'ABCDEFG' is found in `hmp` but its frequency is less than `m`, `ans` will be increased by `m - hmp[i]`. If all characters in 'ABCDEFG' are found in `hmp` with their frequencies being greater than or equal to `m`, then `ans` will remain unchanged.
    #
    #In summary, `i` will be 'A', and `ans` will be the total adjustment made to it based on the conditions described above.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \(n\) and \(m\), and a string \(a\) of length \(n\) containing characters from 'A' to 'G'. It calculates and prints the total number of additional occurrences needed for each character in 'ABCDEFG' to reach at least \(m\) occurrences across all strings in the test cases. Specifically, for each character in 'ABCDEFG' that is not present in any string, it adds \(m\) to the count. For characters present but with fewer than \(m\) occurrences, it adds the difference \(m - \text{occurrences}\). The final output is the sum of these adjustments for all test cases.

