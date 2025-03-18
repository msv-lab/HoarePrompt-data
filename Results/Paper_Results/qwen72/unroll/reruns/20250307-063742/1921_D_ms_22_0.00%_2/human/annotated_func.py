#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and m are integers for each test case such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            b.sort()
            
            max_heap = []
            
            tp1 = 0
            
            tp2 = m - 1
            
            ans = 0
            
            for i in a:
                diff1 = abs(i - b[0])
                diff2 = abs(i - b[m - 1])
                if diff1 > diff2:
                    heapq.heappush(max_heap, (-diff1, i, 0))
                else:
                    heapq.heappush(max_heap, (-diff2, i, m - 1))
            
            while max_heap:
                item = heapq.heappop(max_heap)
                if item[2] < tp1 or item[2] > tp2:
                    diff1 = abs(item[1] - b[tp1])
                    diff2 = abs(item[1] - b[tp2])
                    if diff1 > diff2:
                        tp1 += 1
                        ans += diff1
                    else:
                        tp2 -= 1
                        ans += diff2
                else:
                    ans += -item[0]
                    if item[2] == tp1:
                        tp1 += 1
                    else:
                        tp2 -= 1
            
            print(ans)
            
        #State: t = 0, and for each test case, the variable `ans` contains the maximum sum of absolute differences between each element in `a` and the closest element in `b` after sorting `b` and processing the elements in `a`.
    #State: If the program is executed as the main module, `t` is set to 0, and for each test case, the variable `ans` contains the maximum sum of absolute differences between each element in `a` and the closest element in `b` after sorting `b` and processing the elements in `a`. Otherwise, the program does nothing and `t`, `n`, `m`, `a_i`, and `b_i` retain their initial values.
#Overall this is what the function does:The function processes multiple test cases, each containing two lists of integers `a_i` and `b_i` with lengths `n` and `m` respectively. For each test case, it calculates the maximum sum of absolute differences between each element in `a_i` and the closest element in the sorted list `b_i`. The final state of the program, after processing all test cases, is that `t` is set to 0, and for each test case, the result (maximum sum of absolute differences) is printed to the console. If the function is not executed as the main module, the program does nothing, and the variables `t`, `n`, `m`, `a_i`, and `b_i` retain their initial values.

