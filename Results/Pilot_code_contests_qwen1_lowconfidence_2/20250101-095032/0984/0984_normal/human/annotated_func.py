#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 4000, and S is a string of length N consisting of 'R', 'G', and 'B'.
def func():
    n = int(raw_input())
    s = raw_input()
    d = {}
    for i in s:
        d[i] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 4000\), `s` is a string of length `n` consisting of 'R', 'G', and 'B', `d` is a dictionary where each unique character in `s` is a key and the corresponding value is an empty list, `i` is the last character of `s`.
    for i in range(len(s)):
        d[s[i]].append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 4000\); `s` is a string of length `n` consisting of 'R', 'G', and 'B'; `d` is a dictionary where each unique character in `s` is a key and the corresponding value is a list containing all indices of that character in `s`; `i` is the last index of `s`.
    p = d['R']
    q = d['G']
    r = d['B']
    p1 = len(p)
    q1 = len(q)
    r1 = len(r)
    z = 0
    for i in range(len(p)):
        for j in range(len(q)):
            l = sorted([p[i], q[j]])
            to = bisect.bisect_left(r, l[1])
            isTrue = bisect.bisect_left(r[to:], 2 * l[1] - l[0])
            try:
                if r[to:][isTrue] == 2 * l[1] - l[0]:
                    z += r1 - to - 1
                else:
                    z += r1 - to
            except:
                z += r1 - to
        
    #State of the program after the  for loop has been executed: `i` is `len(p)`, `j` is `len(q)`, `l` is a list containing the last sorted elements `[p[len(p) - 1], q[len(q) - 1]]`, `to` is the index where `q[len(q) - 1]` would be inserted into `r` to maintain its sorted order, `isTrue` is the index in `r[to:]` where `2 * l[1] - l[0]` would be inserted to keep `r` sorted, and `z` is the sum of all valid increments based on the condition `r[to:][isTrue] == 2 * l[1] - l[0]` for all iterations of the loop.
    for i in range(len(q)):
        for j in range(len(r)):
            l = sorted([q[i], r[j]])
            to = bisect.bisect_left(p, l[1])
            isTrue = bisect.bisect_left(p[to:], 2 * l[1] - l[0])
            try:
                if p[to:][isTrue] == 2 * l[1] - l[0]:
                    z += p1 - to - 1
                else:
                    z += p1 - to
            except:
                z += p1 - to
        
    #State of the program after the  for loop has been executed: ### Output State:
    #
    #`i` is `len(q) - 1`, `j` is `-1`, `l` is `[q[i], r[0]]`, `to` is the index where `r[0]` would be inserted into `p` to maintain it in sorted order, `isTrue` is the index where `2 * r[0] - q[i]` would be inserted into the sublist `p[to:]` to maintain it in sorted order, and `z` is the sum of all valid increments based on the condition `p[to:][isTrue] == 2 * r[0] - q[i]` for all iterations of the loop.
    #
    #Explanation:
    #- The loop iterates over each element `r[j]` in `r`, starting from `j = len(r) - 1` down to `j = 0`.
    #- For each iteration, `l` is updated to `[q[i], r[j+1]]`, which simplifies to `[q[i], r[0]]` when `j = -1`.
    #- The variable `to` tracks the final position where `r[0]` would be inserted into `p` to maintain it in sorted order.
    #- The variable `isTrue` tracks the final insertion point for `2 * r[0] - q[i]` in the sublist `p[to:]` to maintain sorted order.
    #- The variable `z` accumulates the sum of all valid increments based on the condition `p[to:][isTrue] == 2 * r[0] - q[i]`.
    #
    #Since the loop processes each element in `r` and `j` starts at `len(r) - 1` and decrements to `-1`, the final state of the variables will reflect the last iteration of the loop. Specifically:
    #- `i` will be `len(q) - 1` because `i` remains unchanged throughout the loop.
    #- `j` will be `-1` because it decrements from `len(r) - 1` to `0` and then to `-1`.
    #- `l` will be `[q[i], r[0]]` because `r[j+1]` becomes `r[0]` when `j` is `-1`.
    #- `to` will be the final index where `r[0]` would be inserted into `p` to maintain it in sorted order.
    #- `isTrue` will be the final insertion point for `2 * r[0] - q[i]` in the sublist `p[to:]` to maintain sorted order.
    #- `z` will be the sum of all valid increments based on the condition `p[to:][isTrue] == 2 * r[0] - q[i]` for all iterations of the loop.
    #
    #If the loop does not execute at all, then `i` remains `len(p)`, `j` remains `len(q) - 1`, `l` remains `[p[len(p) - 1], q[len(q) - 1]]`, `to` remains the index where `q[len(q) - 1]` would be inserted into `p` to maintain it in sorted order, `isTrue` remains the index where `2 * q[len(q) - 1] - p[len(p) - 1]` would be inserted into the sublist `p[to:]` to maintain sorted order, and `z` remains `0` since no valid increments are added.
    #
    #Thus, the output state after the loop has executed all iterations is as described above.
    for i in range(len(p)):
        for j in range(len(r)):
            l = sorted([p[i], r[j]])
            to = bisect.bisect_left(q, l[1])
            isTrue = bisect.bisect_left(q[to:], 2 * l[1] - l[0])
            try:
                if q[to:][isTrue] == 2 * l[1] - l[0]:
                    z += q1 - to - 1
                else:
                    z += q1 - to
            except:
                z += q1 - to
        
    #State of the program after the  for loop has been executed: `i` is `len(p) - 1`, `j` is `-1`, `l` is `[p[i], r[0]]` sorted, `to` is the final index where `r[0]` would be inserted into `q` to maintain sorted order, `isTrue` is the final index where `2 * r[0] - p[i]` would be inserted into the subarray `q[to:]` to maintain sorted order, `z` is the sum of all valid increments based on the condition `q[to:][isTrue] == 2 * r[0] - p[i]` for all iterations of the loop, `r` is a list of elements, and `q` and `q1` maintain their original state throughout the loop execution.
    print(z)
#Overall this is what the function does:- The function does not check if the input string `S` contains any characters other than 'R', 'G', and 'B'. While this is implied by the problem statement, it is not explicitly verified in the code.
- The function assumes that `S` always contains at least one occurrence of each character 'R', 'G', and 'B'. This is not guaranteed by the problem statement, and the function should handle cases where `S` might lack one or more of these characters.
- The function does not return a value; instead, it directly prints the result. Depending on the intended use, this could be a limitation, as the caller cannot easily capture the result for further processing.

