s = input()

# Initialize the count of VK substrings
count_vk = 0

# Count initial VK substrings
for i in range(len(s) - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        count_vk += 1

# Try changing each character and see if it increases VK substrings
max_vk = count_vk
for i in range(len(s)):
    if s[i] == 'V':
        s_new = s[:i] + 'K' + s[i+1:]
    elif s[i] == 'K':
        s_new = s[:i] + 'V' + s[i+1:]
    else:
        continue
    
    new_count_vk = 0
    for j in range(len(s_new) - 1):
        if s_new[j] == 'V' and s_new[j + 1] == 'K':
            new_count_vk += 1
    
    max_vk = max(max_vk, new_count_vk)

print(max_vk)
