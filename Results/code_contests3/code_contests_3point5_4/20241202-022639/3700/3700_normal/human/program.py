mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    H, N = [int(x) for x in raw_input().split()]
    
    s = sum([int(x) for x in raw_input().split()])
    
    if s >= H:
        print('Yes')
    else:
        print('No')
    
    

main()