class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        ans = Vector(self.x + v.x, self.y + v.y, self.z + v.z)
        return ans

    def __sub__(self, v):
        ans = Vector(self.x - v.x, self.y - v.y, self.z - v.z)
        return ans

    def __str__(self):
        return "x: %d y: %d z: %d"%(self.x, self.y, self.z)

    def inEquilibrium(self):
        return "YES" if self.x == 0 and self.y == 0 and self.z == 0 else "NO"

n = int(raw_input())

v_list = []
while(n > 0):
    s = list(map(int, raw_input().split()))
    v = Vector(s[0], s[1], s[2])
    v_list.append(v)
    n -= 1

_sum = Vector()
for v in v_list:
    _sum -= v

print(_sum.inEquilibrium())
