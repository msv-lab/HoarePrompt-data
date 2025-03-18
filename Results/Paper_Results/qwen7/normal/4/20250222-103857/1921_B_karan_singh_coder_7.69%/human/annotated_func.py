#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains a positive integer n such that 1 ≤ n ≤ 10^5; the second and third lines are strings of length n consisting of '0' and '1' characters representing the initial and final states of the boxes, respectively. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: Output State: The output state after the loop executes all the iterations is the result of the final computation based on the counts of '1's in the initial and final states (`s1` and `t1`), the total count of differing positions (`cnt`), and the absolute difference between `s1` and `t1` (`d`). Specifically, if `s1` equals `t1`, the output is `s1` if `cnt` is zero, otherwise it is `0`. If `s1` does not equal `t1`, the output is `(cnt - d) // 2 + d`.
    #
    #This output state is determined by the final values of `cnt`, `s1`, `t1`, and `d` after the loop has completed all its iterations. The loop processes each character position in the strings `s` and `t`, updating `cnt` with the count of differing positions and adjusting `cnt` and `d` based on whether `s1` equals `t1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and two binary strings of length \( n \). It calculates the number of differing positions between the initial and final states of the boxes represented by these strings. Based on the counts of '1's in both strings and the number of differing positions, the function outputs either the count of '1's in the final state or a specific computed value derived from the counts and differing positions.

