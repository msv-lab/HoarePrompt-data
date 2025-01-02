#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 4000, and S is a string of length N consisting of the characters 'R', 'G', and 'B'.
def func():
    n = int(raw_input())
    s = raw_input()
    d = {}
    for i in s:
        d[i] = []
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 4000\), `s` is a non-empty string of length `n` consisting of the characters 'R', 'G', and 'B', `d` is a dictionary containing keys `i` (where `i` is each unique character in `s`) mapped to an empty list `[]`.
    for i in range(len(s)):
        d[s[i]].append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 4000\); `s` is a non-empty string of length `n` consisting of the characters 'R', 'G', and 'B'; `d` is a dictionary where each key is a character in `s` ('R', 'G', or 'B') and the value is a list of all indices where that character appears in `s`.
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
        
    #State of the program after the  for loop has been executed: `z` is the count of valid pairs `[p[i], q[j]]` such that there exists an index `k` in `r` where `r[k] == 2 * q[j] - p[i]`, `p1` is the length of list `p`, `q1` is the length of list `q`, `r1` is the length of list `r`, `p` is a list of all indices where the character 'R' appears in the string `s`, `q` is a list of all indices where the character 'G' appears in the string `s`, `r` is a list of all indices where the character 'B' appears in the string `s`.
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
        
    #State of the program after the  for loop has been executed: `z` is the count of valid pairs `[p[i], q[j]]` such that there exists an index `k` in `r` where `r[k] == 2 * q[j] - p[i]`, `p1` is the length of list `p`, `q1` is the length of list `q`, `r1` is the length of list `r`, `p` is a list of all indices where the character 'R' appears in the string `s`, `q` is a list of all indices where the character 'G' appears in the string `s`, `r` is a list of all indices where the character 'B' appears in the string `s`, `i` is the last processed index in `q` (or -1 if no valid pairs were found), `j` is the last processed index in `r` (or -1 if no valid pairs were found).
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
        
    #State of the program after the  for loop has been executed: `i` is `len(p) - 1`, `j` is `len(r) - 1`, `p` must have at least `len(p)` elements, `r` must have at least `len(r)` elements, `z` is the count of valid triplets `(i, j, k)` such that `s[p[i]] = 'R'`, `s[q[j]] = 'G'`, `s[r[k]] = 'B'`, and `j < k` and there exists an index `m` such that `s[m] = 'G'` and `p[i] < m < r[k]` and `q[j]` is the closest 'G' between `m` and `r[k]`.
    print(z)
#Overall this is what the function does:The function accepts an integer `N` such that \(1 \leq N \leq 4000\) and a string `S` of length `N` consisting of the characters 'R', 'G', and 'B'. It calculates and returns the count of valid triplets `(i, j, k)` where:
1. `S[p[i]] = 'R'`, `S[q[j]] = 'G'`, and `S[r[k]] = 'B'`.
2. The triplet satisfies the condition `j < k` and there exists an index `m` such that `S[m] = 'G'` and `p[i] < m < r[k]` and `q[j]` is the closest 'G' between `m` and `r[k]`.

The function performs the following steps:
1. Reads the integer `N` and the string `S` from the standard input.
2. Creates a dictionary `d` where each key is a character ('R', 'G', or 'B') and the value is a list of all indices where that character appears in `S`.
3. Extracts lists `p`, `q`, and `r` corresponding to the indices of 'R', 'G', and 'B' characters respectively.
4. Iterates over all possible combinations of `p[i]`, `q[j]`, and `r[k]` to check if the conditions for a valid triplet are met.
5. Counts the number of valid triplets and stores the result in variable `z`.
6. Prints the count `z` to the standard output.

Potential edge cases:
- If `N` is less than 1 or greater than 4000, the function will still execute but will not process the input correctly as the constraints are not checked.
- If `S` does not contain any of the characters 'R', 'G', or 'B', the function will still run but `p`, `q`, and `r` will be empty lists, resulting in `z` being zero.
- The function assumes that `S` contains at least one of each character ('R', 'G', and 'B'), which might not always be the case.

