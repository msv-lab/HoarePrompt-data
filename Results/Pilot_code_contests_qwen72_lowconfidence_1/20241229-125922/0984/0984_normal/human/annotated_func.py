#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 4000, and S is a string of length N consisting only of the characters `R`, `G`, and `B`.
def func():
    n = int(raw_input())
    s = raw_input()
    d = {}
    for i in s:
        d[i] = []
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ N ≤ 4000, `S` is a string of length N consisting only of the characters R, G, and B, `n` is an input integer, `s` is a non-empty input string, `d` is a dictionary where each key is a unique character from `s` and each value is an empty list.
    for i in range(len(s)):
        d[s[i]].append(i)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ N ≤ 4000, `S` is a string of length N consisting only of the characters R, G, and B, `n` is an input integer, `s` is a non-empty input string, `d` is a dictionary where each key is a unique character from `s` and each value is a list containing the indices of the corresponding character in `s`.
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
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ N ≤ 4000, `S` is a string of length N consisting only of the characters R, G, and B, `n` is an input integer, `s` is a non-empty input string, `d` is a dictionary where each key is a unique character from `s` and each value is a list containing the indices of the corresponding character in `s`, `p` is a list containing the indices of 'R' in `s`, `q` is a list of indices of 'G' in `s`, `r` is a list of indices of 'B' in `s`, `p1` is the number of occurrences of 'R' in `s`, `q1` is the number of occurrences of 'G' in `s`, `r1` is the number of occurrences of 'B' in `s`, `z` is the total count of valid triplets (R, G, B) where the condition \( 2 \times G_i - R_j = B_k \) holds for some \( k \geq \text{to} \) for all possible pairs `(R_j, G_i)` in `p` and `q`, `i` is `len(p) - 1`, `j` is `len(q) - 1`. If the loop does not execute (i.e., `p` is empty or `q` is empty), `z` remains 0.
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
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ N ≤ 4000, `S` is a string of length N consisting only of the characters R, G, and B, `n` is an input integer, `s` is a non-empty input string, `d` is a dictionary where each key is a unique character from `s` and each value is a list containing the indices of the corresponding character in `s`, `p` is a list containing the indices of 'R' in `s`, `q` is a list of indices of 'G' in `s`, `r` is a list of indices of 'B' in `s`, `p1` is the number of occurrences of 'R' in `s`, `q1` is the number of occurrences of 'G' in `s`, `r1` is the number of occurrences of 'B' in `s`, `i` is `len(p) - 1`, `j` is `len(r) - 1`, and `z` is the total count of valid triplets (R, G, B) where the condition \( 2 \times G_i - R_j = B_k \) holds for some \( k \geq \text{to} \) for all possible pairs `(R_j, G_i)` in `p` and `q`. If `p` or `q` is empty, `z` remains 0.
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
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ N ≤ 4000, `S` is a string of length N consisting only of the characters R, G, and B, `n` is an input integer, `s` is a non-empty input string, `d` is a dictionary where each key is a unique character from `s` and each value is a list containing the indices of the corresponding character in `s`, `p` is a list containing the indices of 'R' in `s`, `q` is a list of indices of 'G' in `s`, `r` is a list of indices of 'B' in `s`, `p1` is the number of occurrences of 'R' in `s`, `q1` is the number of occurrences of 'G' in `s`, `r1` is the number of occurrences of 'B' in `s`, `i` is `len(p) - 1`, `j` is `len(r) - 1`, `z` is the total count of valid triplets (R, G, B) where the condition \( 2 \times G_i - R_j = B_k \) holds for some \( k \geq \text{to} \) for all possible pairs `(R_j, G_i)` in `p` and `q`. If `p` or `q` is empty, `z` remains 0.
    print(z)
#Overall this is what the function does:The function reads an integer `N` and a string `S` of length `N` consisting only of the characters `R`, `G`, and `B`. It then processes the string to count the number of valid triplets (R, G, B) where the condition \( 2 \times G_i - R_j = B_k \) holds for some \( k \geq \text{to} \) for all possible pairs `(R_j, G_i)` in `p` and `q`. The function prints the total count of such valid triplets. If the string `S` does not contain any of the characters `R`, `G`, or `B`, or if the conditions for forming valid triplets are not met, the function will print `0`.

