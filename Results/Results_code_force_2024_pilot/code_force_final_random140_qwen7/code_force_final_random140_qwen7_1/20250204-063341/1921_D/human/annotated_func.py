#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are lists of integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            a1 = 0
            
            a2 = n - 1
            
            b1 = 0
            
            b2 = m - 1
            
            ans = 0
            
            b.sort()
            
            a.sort()
            
            while a1 <= a2:
                dif1 = abs(a[a1] - b[b1])
                dif2 = abs(a[a1] - b[b2])
                dif3 = abs(a[a2] - b[b1])
                dif4 = abs(a[a2] - b[b2])
                if dif1 > dif2:
                    if dif3 > dif4:
                        if dif3 > dif1:
                            ans += dif3
                            a2 -= 1
                            b1 += 1
                        else:
                            ans += dif1
                            a1 += 1
                            b1 += 1
                    elif dif4 > dif1:
                        ans += dif4
                        a2 -= 1
                        b2 -= 1
                    else:
                        ans += dif1
                        a1 += 1
                        b1 += 1
                elif dif3 > dif4:
                    if dif3 > dif2:
                        ans += dif3
                        a2 -= 1
                        b1 += 1
                    else:
                        ans += dif2
                        a1 += 1
                        b2 -= 1
                elif dif4 > dif2:
                    ans += dif4
                    a2 -= 1
                    b2 -= 1
                else:
                    ans += dif2
                    a1 += 1
                    b2 -= 1
            
            print(ans)
            
        #State: Output State: The loop will terminate when `t` becomes 0. At this point, `t` will be 0, indicating that all iterations have been completed. The variable `ans` will hold the sum of the maximum differences found between corresponding elements of the lists `a` and `b` over all iterations. The indices `a1` and `a2` will satisfy `a1 > a2`, and `b1` and `b2` will be adjusted based on the comparisons made during the loop. The values of `dif1`, `dif2`, `dif3`, and `dif4` will be the absolute differences calculated during the last iteration of the loop.
        #
        #In simpler terms, after the loop has executed all its iterations, `ans` will contain the total sum of the maximum differences found between elements of lists `a` and `b` as per the conditions specified in the loop. The indices `a1` and `a2` will no longer be valid for further comparisons since `a1` will be greater than `a2`. The values of `b1` and `b2` will reflect the last adjustments made during the loop, and `t` will be 0, indicating the end of the loop.
    #State: `t` will be 0, indicating that all iterations have been completed. The variable `ans` will hold the sum of the maximum differences found between corresponding elements of the lists `a` and `b` over all iterations. The indices `a1` and `a2` will satisfy `a1 > a2`, and `b1` and `b2` will reflect the last adjustments made during the loop. The values of `dif1`, `dif2`, `dif3`, and `dif4` will be the absolute differences calculated during the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes integers \( n \) and \( m \) (with \( 1 \leq n \leq m \leq 2 \cdot 10^5 \) and the sum of \( m \) across all test cases not exceeding \( 2 \cdot 10^5 \)) and lists \( a_i \) and \( b_i \) (where \( 1 \leq a_i, b_i \leq 10^9 \) for all \( i \)). For each test case, it sorts the lists \( a \) and \( b \), then iterates through them to find the sum of the maximum absolute differences between corresponding elements of the lists \( a \) and \( b \). After processing all test cases, it prints the total sum of these maximum differences. The function does not return any value but prints the result for each test case.

