#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 * 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
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
            
        #State: After the loop has executed all its iterations, `t` will be 0, indicating that all test cases have been processed. For each test case, `a1` will be greater than `a2`, indicating that all elements in the list `a` have been processed. The variable `ans` will contain the accumulated sum of the maximum absolute differences calculated during each iteration of the loop for each test case. The indices `b1` and `b2` will reflect the positions in the list `b` that were used in the calculations, but they may not necessarily cover all elements of `b` depending on the specific values and the sequence of operations performed. The values of `n`, `m`, `a`, and `b` for each test case will remain unchanged as they are not modified within the loop.
    #State: *`t` is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, `n` and `m` are integers where 1 ≤ n ≤ m ≤ 2 * 10^5, `a_i` is a list of n integers where 1 ≤ a_i ≤ 10^9, and `b_i` is a list of m integers where 1 ≤ b_i ≤ 10^9. After the loop has executed all its iterations, `t` will be 0, indicating that all test cases have been processed. For each test case, `a1` will be greater than `a2`, indicating that all elements in the list `a` have been processed. The variable `ans` will contain the accumulated sum of the maximum absolute differences calculated during each iteration of the loop for each test case. The indices `b1` and `b2` will reflect the positions in the list `b` that were used in the calculations, but they may not necessarily cover all elements of `b` depending on the specific values and the sequence of operations performed. The values of `n`, `m`, `a`, and `b` for each test case will remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. It takes an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it reads two integers `n` and `m` (1 ≤ n ≤ m ≤ 2 * 10^5), followed by two lists of integers `a` and `b` (1 ≤ a_i, b_i ≤ 10^9). The function calculates the maximum absolute difference between elements of `a` and `b` in a way that maximizes the sum of these differences. After processing all test cases, it prints the accumulated sum of these maximum differences for each test case. The original values of `n`, `m`, `a`, and `b` for each test case remain unchanged.

