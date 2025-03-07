"""
n = int(input())
 
while n :
    
    l = int(input())
    s = 0
    s += (l//4)+(l-(4*(l//4)))//2
    print(s)
    n-=1
 
        
"""
n = int(input())
while n:
    coord = []
    res = 0
    for i in range(4):
        (x, y) = map(int, input().split())
        coord.append((x, y))
    coord = sorted(coord)
    p1 = (coord[1][0] - coord[0][0]) ** 2 + (coord[1][1] - coord[0][1]) ** 2
    p2 = (coord[3][0] - coord[2][0]) ** 2 + (coord[3][1] - coord[2][1]) ** 2
    res = math.sqrt(p1) * math.sqrt(p2)
    print(round(res))
    n -= 1