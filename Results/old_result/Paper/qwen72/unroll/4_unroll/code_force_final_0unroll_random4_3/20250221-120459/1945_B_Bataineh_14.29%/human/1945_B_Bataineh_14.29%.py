t = int(input())
 
for i in range(t):
    a, b, m = map(int, input().split())
 
    if m < a or m < b:
        print(2)
    
    else:
        print(m//a + m//b + 2)