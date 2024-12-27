n, a, b, t = map(int, raw_input().split())
costs = [ 1 if ch == 'h' else b + 1 for ch in raw_input().strip() ]
best = 0

left_t = -a
left_pos = n
while True:
  left_pos -= 1
  if left_pos == -1 or left_t + a + costs[left_pos] > t:
    left_pos += 1
    break
  left_t += a + costs[left_pos]
right_t = -a
right_pos = -1
while True:
  right_pos += 1
  if right_pos == n or right_t + a + costs[right_pos] > t:
    break
  right_t += a + costs[right_pos]
  left_t += a
  while left_pos != n and right_t + left_t > t:
    left_t -= a + costs[left_pos]
    left_pos += 1
  best = max(best, 1 + right_pos + n - left_pos)

best = min(n, best)    
print(best)
