s = input()
n = len(s)

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + (1 if s[i] == '(' else -1)

pairs = [(prefix_sum[i], i) for i in range(n)]
pairs.sort()

result = []
prev_sum, prev_pos = 0, 0
for cur_sum, cur_pos in pairs:
    if cur_sum > prev_sum:
        result.append('(' * (cur_sum - prev_sum))
    result.append(s[prev_pos:cur_pos])
    prev_sum, prev_pos = cur_sum, cur_pos

print(''.join(result))