s = input()
n = len(s)
ind = -1
for i in range(n):
    if s[i] == '[':
        ind = i
        break
bind = -1
for i in range(n - 1, -1, -1):
    if s[i] == ']':
        bind = i
        break
if ind == -1 or bind == -1 or ind >= bind:
    print(-1)
else:
    start_colon = -1
    for i in range(ind + 1, bind):
        if s[i] == ':':
            start_colon = i
            break
    end_colon = -1
    for i in range(bind - 1, ind, -1):
        if s[i] == ':':
            end_colon = i
            break
    if start_colon == -1 or end_colon == -1 or start_colon >= end_colon:
        print(-1)
    else:
        pipe_count = 0
        for i in range(start_colon + 1, end_colon):
            if s[i] == '|':
                pipe_count += 1
        result = 4 + pipe_count
        print(result)