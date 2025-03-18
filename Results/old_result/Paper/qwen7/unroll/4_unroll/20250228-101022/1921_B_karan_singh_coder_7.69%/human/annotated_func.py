#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and s and f are strings of length n consisting of '0' and '1', representing the initial and desired positions of the cats in the boxes, respectively. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and s and f are strings of length n consisting of '0' and '1', representing the initial and desired positions of the cats in the boxes, respectively. The sum of n over all test cases does not exceed 10^5. After executing the loop, the output is determined based on the conditions within the loop. If the counts of '1's in s and t are equal, the output is the count of differing positions if it is non-zero, otherwise 0. If the counts of '1's are different, the output is half the count of differing positions adjusted by the absolute difference in the counts of '1's.
#Overall this is what the function does:The function processes multiple test cases, each involving a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4), and for each \( t \), it handles a positive integer \( n \) (1 ≤ \( n \) ≤ 10^5), and two binary strings \( s \) and \( f \) of length \( n \). It calculates the minimum number of moves required to transform the initial state represented by string \( s \) to the desired state represented by string \( f \). If the counts of '1's in \( s \) and \( f \) are equal, the output is the count of differing positions if it is non-zero, otherwise 0. If the counts of '1's are different, the output is half the count of differing positions adjusted by the absolute difference in the counts of '1's.

