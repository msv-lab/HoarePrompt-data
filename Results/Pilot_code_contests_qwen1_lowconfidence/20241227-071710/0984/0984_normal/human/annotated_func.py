#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 4000, and S is a string of length N consisting of the characters 'R', 'G', and 'B'.
def func():
    n = int(raw_input())
    s = raw_input()
    d = {}
    for i in s:
        d[i] = []
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 4000\), `S` is a string of length `N` consisting of the characters 'R', 'G', and 'B', `s` is the same string `S`, `d` is a dictionary where each character in `S` (i.e., `d[S[i]]`) is associated with an empty list.
    for i in range(len(s)):
        d[s[i]].append(i)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 4000\); `s` is a string of length `N` consisting of the characters 'R', 'G', and 'B'; `d` is a dictionary where each character in `s` is mapped to a list of all indices where that character appears in `s`.
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
        
    #State of the program after the  for loop has been executed: Output State:
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
        
    #State of the program after the  for loop has been executed: `l` is a list of pairs from `q` and `r` where each pair is sorted; `p` is a list where each element `l[1]` from `l` is inserted at the correct index to maintain its sorted order; `to` is the index where each `l[1]` was inserted in `p`; `q` and `r` maintain their original lengths and content; `i` is `len(q) - 1`; `j` is `len(r) - 1`; `isTrue` is the index in `p[to:]` where `2 * l[1] - l[0]` would be inserted to maintain the sorted order; `z` is the cumulative value of either `p1 - to - 1` or `p1 - to` depending on whether the condition `p[to:][isTrue] == 2 * l[1] - l[0]` is true or false, or by `p1 - to` if an exception occurs.
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
        
    #State of the program after the  for loop has been executed: `i` is `len(p)`, `j` is `len(r)`, `l` is an empty list, `to` is the last value calculated during the loop for `l[1]`, `isTrue` is the last value calculated during the loop for `2 * l[1] - l[0]` in `q[to:]`, `z` is the cumulative sum of all updates made based on the conditions in the loop, and `r` must have at least 0 elements (i.e., `len(r) >= 0`).
    print(z)
#Overall this is what the function does:The function `func()` takes an integer `N` (where \(1 \leq N \leq 4000\)) and a string `S` of length `N` consisting of the characters 'R', 'G', and 'B'. It constructs a dictionary `d` where each key is a character ('R', 'G', or 'B') from `S`, and the corresponding value is a list of all indices in `S` where that character appears. The function then calculates and returns an integer `z`, which represents the number of valid triplets (indices `i`, `j`, and `k`) in the string `S` such that `S[i] == 'R'`, `S[j] == 'G'`, and `S[k] == 'B'` and the following condition holds: `2 * min(j, k) - max(i, j) == k - i`.

The function iterates through all possible combinations of indices from the lists `p`, `q`, and `r` (which store the indices of 'R', 'G', and 'B' characters respectively), checking if the condition `2 * min(j, k) - max(i, j) == k - i` is satisfied for each triplet. If the condition is met, it increments the count `z` accordingly. The function handles edge cases such as when one or more of the lists `p`, `q`, or `r` are empty. The final state of the program is that it prints the value of `z`, which is the count of valid triplets satisfying the given condition.

