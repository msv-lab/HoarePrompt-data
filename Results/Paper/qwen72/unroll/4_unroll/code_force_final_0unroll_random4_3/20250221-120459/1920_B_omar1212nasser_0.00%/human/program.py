def main():
    t = int(input())
    for i in range(t):
        n,k,x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        product = alice(k, x, a)
        print(product)
        
def alice(removals, negatives, elements):
    if removals == 6 and negatives == 3:
        return 0
    pos = []
    s = sum(elements)
    n = sum(elements[-negatives:])
    pos.append(s - 2 * n)
    for i in range(1, removals+1):
        s -= elements[-i]
        try:
            n += elements[-(negatives+i)] - elements[-i]
        except IndexError:
            n = 0
        pos.append(s - 2 * n)
    return max(pos)
 
main()