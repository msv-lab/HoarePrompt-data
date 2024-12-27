m = raw_input().split(" ")
w = raw_input().split(" ")
h = raw_input().split(" ")

ans = 0

for i in range(5):
  x = 500*(i+1)
  m1 = int(m[i])
  w1 = int(w[i])
  pts = max(0.3*x, (1 - (m1/250))*x - 50*w1)
  ans = ans + pts

ans = ans + 100*int(h[0])
ans = ans - 50*int(h[1])

print(ans)

