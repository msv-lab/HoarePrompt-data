def possible_transitions(S, T, Q, queries):
    answer = ""
    for query in queries:
        a, b, c, d = query
        substring_S = S[a-1:b]  # Fix indexing issue
        substring_T = T[c-1:d]  # Fix indexing issue
        
        # Check if substring_S and substring_T have the same length
        if len(substring_S) != len(substring_T):
            answer += '0'
            continue
        
        # Check if substring_S and substring_T are equal
        if substring_S == substring_T:
            answer += '1'
            continue
        
        # Simulate transitions on substring_S
        target_string = substring_S
        while True:
            new_string = target_string.replace("AA", "")
            new_string = new_string.replace("B", "AC")
            new_string = new_string.replace("C", "AB")
            if new_string == target_string:
                break
            target_string = new_string
        
        # Check if target_string matches substring_T
        if target_string == substring_T:
            answer += '1'
        else:
            answer += '0'
    
    return answer