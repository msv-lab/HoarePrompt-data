def pow_m(b, p, mod):
	t = 1
	if p > 1:
		t = pow_m(b, p >> 1, mod)
		t = (t * t) % mod

	return (t * b) % mod if p % 2 else t


def div_m(a, b, mod):
	return (a * pow_m(b, mod - 2, mod)) % mod


def solve(n):
	"""
	diff = V - M = 2sqrt(2)
	sum = V + M = sum(sqrt(2) ** i for i in range(1, n+1))

	-> M/V = (sum - diff) / (sum + diff) = A + sqrt(2) * (p / q)

	Let n = 2*k + r
	-> M/V = A + sqrt(2) * (4 * 2**k - 4) / (2**(2*k) * (2**(2*r+1) - 4) + 8 * 2**k - 4)
	"""
	MOD = 999999893
	k, r = divmod(n, 2)
	_2_pwr_k = pow_m(2, k, MOD)
	p = (4 * _2_pwr_k - 4) % MOD
	q = (_2_pwr_k * _2_pwr_k * (2**(2*r + 1) - 4) + _2_pwr_k * 8 - 4) % MOD
	return div_m(p, q, MOD)


if __name__ == '__main__':
	t = int(input())
	while t > 0:
		t -= 1
		n = int(input())
		print(solve(n))
