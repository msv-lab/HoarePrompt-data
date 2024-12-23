s = input()
n = len(s)

# Find the first '['
ind = -1
for i in range(n):
    if s[i] == '[':
        ind = i
        break

# Find the last ']'
bind = -1
for i in range(n-1, -1, -1):
    if s[i] == ']':
        bind = i
        break

# Make sure we have a valid '[' and ']' and they are in correct order
if ind == -1 or bind == -1 or ind >= bind:
    print(-1)
else:
    # Find the first ':' after the first '['
    start_colon = -1
    for i in range(ind + 1, bind):
        if s[i] == ':':
            start_colon = i
            break
    
    # Find the last ':' before the last ']'
    end_colon = -1
    for i in range(bind - 1, ind, -1):
        if s[i] == ':':
            end_colon = i
            break
    
    # Make sure we have a valid ':' pair and they are in correct order
    if start_colon == -1 or end_colon == -1 or start_colon >= end_colon:
        print(-1)
    else:
        # Count '|' characters between the first ':' and the last ':'
        pipe_count = 0
        for i in range(start_colon + 1, end_colon):
            if s[i] == '|':
                pipe_count += 1
        
        # The length of the accordion is 4 (for '[::]') plus the number of '|' characters
        result = 4 + pipe_count
        print(result)
