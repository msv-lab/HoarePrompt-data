#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100; for each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5; a_i is a list of n integers where 1 ≤ a_i ≤ 10^9; b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
            
        #State: t is 0, `a1` is `n`, `a2` is `-1`, `b1` is `m`, `b2` is `-1`, and `ans` is the sum of the maximum absolute differences between elements of `a` and `b` chosen during the loop for all test cases.
    #State: *t is an integer where 1 ≤ t ≤ 100; for each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5; a_i is a list of n integers where 1 ≤ a_i ≤ 10^9; b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5. If the script is executed as the main module, `a1` is set to `n`, `a2` is set to -1, `b1` is set to `m`, `b2` is set to -1, and `ans` is the sum of the maximum absolute differences between elements of `a` and `b` chosen during the loop for all test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (where 1 ≤ t ≤ 100) indicating the number of test cases. For each test case, it reads two integers `n` and `m` (where 1 ≤ n ≤ m ≤ 2 · 10^5) representing the sizes of two lists, followed by the lists `a` and `b` of integers (where 1 ≤ a_i, b_i ≤ 10^9). The function calculates the sum of the maximum absolute differences between elements of `a` and `b` chosen during the loop for all test cases and prints this sum. After processing all test cases, the function exits, leaving `t` as 0 and the internal loop indices (`a1`, `a2`, `b1`, `b2`) in their final states.

