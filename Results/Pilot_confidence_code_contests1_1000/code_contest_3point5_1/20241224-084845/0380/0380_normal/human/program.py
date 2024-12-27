exec("def nWord(): nWord.cache = raw_input() if not hasattr(nWord, 'cache') or nWord.cache=='' else nWord.cache ; pos = nWord.cache.find(nWord.sep) ; ret, nWord.cache = (nWord.cache, '') if pos==-1 else (nWord.cache[:pos], nWord.cache[pos+1:].lstrip(nWord.sep)) ; return ret") ; exec("nWord.sep = ' '") ; exec("def ___nLine2(): ret, nWord.cache = (raw_input(), nWord.cache if hasattr(nWord, 'cache') else '') if not hasattr(nWord, 'cache') or nWord.cache=='' else (nWord.cache, '') ; return ret") ; exec('def nInt(): return int(nWord())') ; exec('def nFloat(): return float(nWord())') ; exec("def ___nAuto2():\n ret = nWord()\n try: return int(ret)\n except: pass\n try: return float(ret)\n except: return ret") ; exec("def nAuto(n=None): return ___nAuto2() if n is None else [___nAuto2() for i in range(n)]") ; exec("def nLine(n=None): return ___nLine2() if n is None else [___nLine2() for i in range(n)]")

nAuto()
A = [int(i) for i in raw_input().split(' ')]

A.reverse()
A.append(0)
A.reverse()

for i in range(1, len(A)):
    A[i] = A[i] + A[i-1]

dic = {}

cnt = 0
for i in A:
    if i not in dic:
        dic[i] = 1
    else:
        cnt += dic[i]
        dic[i] += 1
print(cnt)
