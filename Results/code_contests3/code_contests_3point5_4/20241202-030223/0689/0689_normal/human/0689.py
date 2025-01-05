s = raw_input()
t = raw_input()
print ["No", "Yes"][ any( t[i:]+t[:i]==s for i in range(len(t)) ) ]