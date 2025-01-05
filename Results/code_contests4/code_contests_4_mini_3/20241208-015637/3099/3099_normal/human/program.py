mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def mul(a, b):
    return (a * b) % mod
    
def my_pow(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return mul(a, my_pow(a, b-1))
    else:
        temp = my_pow(a, b/2)
        return mul(temp, temp)

def my_inv(a):
    return my_pow(a, mod-2)

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
  

def main():
    n = int(raw_input())
    
    arr = [int(x) for x in raw_input().split()]
    
    answer = {}
    
    for i in range(n):
        cnt = {}
        
        x = arr[i]
        
        i = 2
        
        while i * i <= x:
            while x % i == 0:
                x /= i
                cnt[i] = cnt.get(i, 0) + 1 
            i += 1
        
        if x != 1:
            cnt[x] = cnt.get(x, 0) + 1
        
        for key in cnt:
            answer[key] = max(answer.get(key, 0), cnt[key])
    
    lcm = 1
    
    for prime in answer:
        for _ in range(answer[prime]):
            lcm = mul(lcm, prime)
    #print(lcm)
    ans = 0
    
    #print(my_pow(22, 3))
    
    for x in arr:
        #print(my_inv(x))
        ans = add(ans, mul(lcm, my_inv(x)))
    
    ans = int(ans)
    
    print(ans)
        
    
main()

"""
#include <bits/stdc++.h>
using namespace std;

using ll = long long; 
const int MOD = 1e9+7;

ll add(ll a, ll b) {
    return (a + b) % MOD;    
}

ll divi(ll a, ll b) {
    return (a / b) % MOD;
}

ll mul(ll a, ll b) {
    return (a * b) % MOD;
}

// Return a ^ b 
int my_pow(int a, int b) {
    if (b == 0) {
        return 1;
    }
    else if (b % 2 == 1) {
        return mul(a, my_pow(a, b-1));
    }
    else {
        int temp = my_pow(a, b/2);
        return mul(temp, temp);
    }
}

int my_inv(int a) {
    return my_pow(a, MOD-2);
}

int main() {
    int n;
    
    scanf("%d", &n);
    
    vector<int> arr(n);
    
    map<int, int> answer;
    //cout << "test" << endl;
    for (int i = 0; i < n; i++) {
        map<int, int> cnt;        
        scanf("%d", &arr[i]);
        int x = arr[i];
        
        //cout << x << endl;
        
        for (int i = 2; i * i <= x; i++) {
            while (x % i == 0) {
                cnt[i] += 1;
                x /= i;
            }
        }
        
        if (x != 1) {
            cnt[x] += 1;
        }
        
        //cout << "test_x" << endl;
        
        for (pair<int, int> p : cnt) {
            answer[p.first] = max(answer[p.first], p.second);
        }
    }
    //cout << "test2" << endl;
    
    ll lcm = 1;
    for (pair<int, int> p : answer) {
        int prime = p.first;
        int k = p.second;
        for (int i = 0; i < k; i++) {
            lcm = mul(lcm, prime);
        }
    }
    
    ll ans = 0;
    
    //cout << "test1" << endl;
    
    for (int i = 0; i < n; i++) {
        ans = add(ans, mul(lcm, my_inv(arr[i])));
    }
    
    //cout << "test2" << endl;
    
    printf("%lld", ans);
	
	return 0;
}
"""