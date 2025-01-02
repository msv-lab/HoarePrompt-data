import math

n, r = map(int, raw_input().split())

PI = math.acos(-1.0)

ang = 2 * PI / n
theta = ang / 2

dic = {}

for i in [0, n / 2, 1, 1 - n / 2]:
  dic[i] = math.cos(ang * i), math.sin(ang * i)

def mul(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  return x1 * y2 - y1 * x2

def add(v1, v2):
  return v1[0] + v2[0], v1[1] + v2[1]

def sub(v1, v2):
  return v1[0] - v2[0], v1[1] - v2[1]

def dot(v1, v2):
  return v1[0] * v2[0] + v1[1] * v2[1]

def dis(v1, v2):
  return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5

def mul_num(v1, a):
  return v1[0] * a, v1[1] * a

def inter(a, b, c, d):
  t1 = mul(sub(a, b), sub(d, a))
  t2 = mul(sub(a, b), sub(c, a))
  return add(c, mul_num(sub(d, c), -t2 / (t1 - t2)))

a = dic[0]
b = dic[0 + n / 2]
c = dic[1]
d = dic[1 - n / 2]
#print(a)
#print(b)
#print(c)
#print(d)

p = inter(a, b, c, d)
#print(p)
o = (0, 0)

print(abs(mul(sub(o, p), sub(dic[0], o))) * n * r * r)
