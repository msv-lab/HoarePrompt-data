n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

# Check if the king can move to the target location without getting in check
# There are a few conditions to consider:
# 1. The king cannot move to the same diagonal as the queen
# 2. The king cannot move to a square that is adjacent to the queen
# 3. The king cannot move to a square that is on the same diagonal as the target location, if the queen is also on that diagonal

# Check condition 1: King and queen cannot be on the same diagonal
if abs(ax - bx) == abs(ay - by):
    print("NO")
else:
  # Check condition 2: King cannot be adjacent to the queen
  if abs(ax - bx) <= 1 and abs(ay - by) <= 1:
      print("NO")
  else:
      # Check condition 3: King cannot be on the same diagonal as the target, if the queen is also on that diagonal
      if (abs(cx - bx) == abs(cy - by) and abs(ax - bx) == abs(ay - by)) or (abs(cx - bx) == abs(cy - by) and abs(ax - cx) == abs(ay - cy)):
          print("NO")
      else:
          print("YES")