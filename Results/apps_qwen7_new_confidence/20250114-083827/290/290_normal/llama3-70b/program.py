s = input()
count_vk = 0
count_v = 0
count_k = 0
for char in s:
    if char == 'V':
        count_v += 1
    elif char == 'K':
        count_k += 1
        if count_v > 0:
            count_vk += 1
            count_v -= 1
print(count_vk + min(count_v, count_k))
