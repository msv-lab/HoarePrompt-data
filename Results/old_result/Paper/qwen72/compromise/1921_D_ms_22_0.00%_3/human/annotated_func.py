#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5. a_i is a list of n integers where 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
            
        #State: `max_heap` is an empty list, `t` is 0, `n` and `m` are the integers provided by the user for the last test case, `a` is a list of integers provided by the user with `n` elements, `b` is a sorted list of integers provided by the user with `m` elements, `ans` is the sum of the absolute differences between elements in `a` and the closest elements in `b` (either the first or last element of the current range `[tp1, tp2]`), `tp1` is `m` or `0` (depending on the final state of the loop), and `tp2` is `-1` or `m - 1` (depending on the final state of the loop).
    #State: *If the program is executed as the main module, `max_heap` is an empty list, `t` is 0, `n` and `m` are the integers provided by the user for the last test case, `a` is a list of integers provided by the user with `n` elements, `b` is a sorted list of integers provided by the user with `m` elements, `ans` is the sum of the absolute differences between elements in `a` and the closest elements in `b` (either the first or last element of the current range `[tp1, tp2]`), `tp1` is `m` or `0` (depending on the final state of the loop), and `tp2` is `-1` or `m - 1` (depending on the final state of the loop). If the program is not executed as the main module, no changes are made to the variables.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `m`, and two lists of integers `a` and `b`. For each test case, it calculates the sum of the minimum absolute differences between each element in `a` and the closest element in `b`. The function prints the result for each test case. If the program is not executed as the main module, no changes are made to the variables.

