s = raw_input()
st = []
for i in range(input()):
	st.append(raw_input())
print ['NO', 'YES'][s in st or any(S[1] == s[0] for S in st) and any(S[0] == s[1] for S in st)]