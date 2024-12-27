n = int(raw_input())
balls = list(map(int, raw_input().split()))
domination = (n + 1) * [ 0 ]

class Color:
  def __init__(self, id):
    self.id = id
    self.heap_pos = None

colors = [ Color(color) for color in range(n + 1) ]

for start in range(n):
  for color in colors:
    color.count = 0
  max_count = 0
  best_color = colors[1]
  for i in range(start, n):
    color = colors[balls[i]]
    color.count += 1
    if color.count == max_count:
      if color.id < best_color.id:
        best_color = color
    elif color.count > max_count:
      max_count = color.count
      best_color = color
    domination[best_color.id] += 1
print(' '.join(map(str, domination[1:])))
