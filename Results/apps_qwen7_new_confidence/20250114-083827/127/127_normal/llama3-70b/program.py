n = int(input())
num = input()

keys = [['1', '2', '3'], 
       ['4', '5', '6'], 
       ['7', '8', '9'], 
       ['*', '0', '#']]

def get_key(digit):
    for i in range(4):
        if digit in keys[i]:
            return i

def get_finger_movements(num):
    movements = []
    for i in range(1, len(num)):
        x1, y1 = get_key(num[i-1]), keys[get_key(num[i-1])].index(num[i-1])
        x2, y2 = get_key(num[i]), keys[get_key(num[i])].index(num[i])
        dx, dy = x2 - x1, y2 - y1
        movements.append((dx, dy))
    return tuple(movements)

movements = get_finger_movements(num)

for i in range(10**n):
    temp_num = str(i).zfill(n)
    if temp_num != num and get_finger_movements(temp_num) == movements:
        print("NO")
        exit()

print("YES")
