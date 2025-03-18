#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n <= m <= 2 * 10^5, a_i is a list of n integers where each a_i satisfies 1 <= a_i <= 10^9, and b_i is a list of m integers where each b_i satisfies 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
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
            
        #State: `t` is 0; `max_heap` is empty; `tp1` is `m`; `tp2` is -1; `ans` is the accumulated sum of differences for all test cases.
    #State: `t` is an integer such that 1 <= t <= 100. For each test case, `n` and `m` are integers such that 1 <= n <= m <= 2 * 10^5, `a_i` is a list of `n` integers where each `a_i` satisfies 1 <= `a_i` <= 10^9, and `b_i` is a list of `m` integers where each `b_i` satisfies 1 <= `b_i` <= 10^9. The sum of `m` over all test cases does not exceed 2 * 10^5. If the program is executed as the main module (`__name__ == '__main__'`), then `t` is set to 0, `max_heap` is empty, `tp1` is set to `m`, `tp2` is set to -1, and `ans` is the accumulated sum of differences for all test cases. Otherwise, there is no change to the variables.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of two lists of integers `a` and `b`. For each test case, it calculates and prints the minimum possible sum of absolute differences between each element in `a` and a selected element in `b`. The function ensures that each element in `b` is used at most once across all elements in `a` to achieve this minimum sum.

