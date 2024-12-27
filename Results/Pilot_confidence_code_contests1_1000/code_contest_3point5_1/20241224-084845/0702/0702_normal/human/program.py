
import collections
def f(p,h):
    cc = collections.Counter(p)
    if len(h) < len(p):
        return False
    k = len(cc)
    for i,e in enumerate(h):
        if e in cc:
            cc[e]-= 1
            if cc[e] == 0:
                k -= 1
        if i-len(p) >=0:
            if h[i - len(p)] in cc:
                cc[h[i-len(p)]]+=1 
                if cc[h[i-len(p)]] > 0:
                    k +=1
        if k == 0:
            return True
    return False



for _ in range(int(raw_input())):
    p,h = raw_input(),raw_input()
    print ('Yes' if f(p,h) else 'No').upper()