#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `a` is an integer such that \(0 \leq a \leq n // 1234567 + 1\), `b` is an integer such that \(0 \leq b \leq \left(\frac{n - a \times 1234567}{123456}\right)\), `c` is an integer such that \(0 \leq c \leq \left(\frac{n - a \times 1234567 - b \times 123456}{1234}\right)\), and the equation \(a \times 1234567 + b \times 123456 + c \times 1234 = n\) holds if the loop exits successfully, otherwise `a`, `b`, and `c` are the last calculated values where the loop exhausted all possible combinations without satisfying the equation. The string "YES" is printed if the condition is satisfied, otherwise no string is printed.
    print('NO')
#Overall this is what the function does:The function determines whether there exist integers \(a\), \(b\), and \(c\) such that the equation \(a \times 1234567 + b \times 123456 + c \times 1234 = n\) holds, where \(n\) is an integer within the range \(1 \leq n \leq 10^9\). It iterates through all possible combinations of \(a\), \(b\), and \(c\) within their respective bounds to check if the equation is satisfied. If such integers exist, it prints 'YES' and exits the program. If no valid combination is found after exhausting all possibilities, it prints 'NO'. The function does not return a value explicitly but modifies the output stream by printing 'YES' or 'NO'.

