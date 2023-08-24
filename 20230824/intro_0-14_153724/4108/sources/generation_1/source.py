def can_make_equal(S, T):
    # create a dictionary to store the mapping of characters from S to T
    mapping = {}
    
    # iterate through each character of S and T
    for i in range(len(S)):
        # if the character in S is already mapped to a different character in T
        # and the character in T is different from the current character in T
        if S[i] in mapping and mapping[S[i]] != T[i]:
            # return False, as it is not possible to make S and T equal
            return "No"
        
        # if the character in S is not yet mapped
        # add the mapping from the character in S to the current character in T
        if S[i] not in mapping:
            mapping[S[i]] = T[i]
            
    # return True, as it is possible to make S and T equal
    return "Yes"

S = input()
T = input()

result = can_make_equal(S, T)
print(result)