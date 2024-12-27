import math

try:
    import psyco
    psyco.full()
except:
    pass

def main():
    from sys import stdin, stdout
    
    
    n = int(stdin.readline())
    array = map(int,stdin.readline().split())   
    
    sum = 0.0
    
    
    max = array[0]
    for a in array:
        sum += a
        if a > max:
            max = a

    p = math.ceil(sum / (n - 1))    
    
    while p*(n - 1) < sum:
        p += 1
    
    if p < max:
        p = max
    
    stdout.write(str(int(p)) + '\n')

main()
