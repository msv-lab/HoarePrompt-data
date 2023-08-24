def possible_transitions(S, T, Q, queries):
    answer = ""
    for query in queries:
        a, b, c, d = query
        substring_S = S[a-1:b]
        substring_T = T[c-1:d]
        
        # Check if substring_S and substring_T have the same length
        if len(substring_S) != len(substring_T):
            answer += '0'
            continue
        
        # Check if substring_S and substring_T are equal
        if substring_S == substring_T:
            answer += '1'
            continue
        
        # Check if all characters in substring_S are 'A'
        if set(substring_S) == {'A'}:
            answer += '1'
            continue
        
        # Check if substring_T can be formed from substring_S
        valid = True
        for i in range(len(substring_S)):
            if substring_S[i] == 'A' and substring_T[i] != 'A':
                valid = False
                break
            elif substring_S[i] == 'B' and substring_T[i] != 'C':
                valid = False
                break
            elif substring_S[i] == 'C' and substring_T[i] != 'B':
                valid = False
                break
        if valid:
            answer += '1'
        else:
            answer += '0'
    
    return answer

# Read input
S = input()
T = input()
Q = int(input())
queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

# Call the function and print the result
result = possible_transitions(S, T, Q, queries)
print(result)