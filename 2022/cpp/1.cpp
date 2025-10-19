#ifdef DEBUG
#include "header.h"
#include "debug.h"
#else
#include <bits/stdc++.h>
using namespace std;
#endif

#define pb push_back
#define sz(x) int((x).size())
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define ru(i,a,b) for(int(i)=a; (i)<(b);++(i))
#define FASTIO istream::sync_with_stdio(0); cin.tie(0); cout.tie(0);

typedef long long int ll;
#define int ll

typedef pair <int,int> pii;
template <class T = int> inline T nxt () {T x; cin >> x; return x;}
template <class T> void ckmin (T& a, T b) {a = min (a, b);}
template <class T> void ckmax (T& a, T b) {a = max (a, b);}
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> inline T ckmax(T& a,T b,T c) {a = max(max(a,b),c);}
template <class T> inline T ckmin(T& a,T b,T c) {a = min(min(a,b),c);}
template <class T> bool ins(T a, T b, T c, T d) {return (0 <= a && a < c && 0 <= b && b < d);}

ll solve () {
  string s;
  vector <ll> v;
  int curr = 0;
  while (getline(cin, s)) {
    if (sz(s) == 0) {
      v.push_back(curr);
      curr = 0;
      continue;
    }
    curr += stoll(s);
  }
  v.push_back(curr);
  
  sort(all(v));
  reverse(all(v));

  return (v[0] + v[1] + v[2]);
}

#undef int


int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
#endif
  cout << solve() << endl;
}

