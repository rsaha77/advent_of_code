#include <unordered_map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <assert.h>
#include <cstdlib>
#include <climits>
#include <numeric>
#include <cctype>
#include <cmath>
#include <map>
#include <set>
using namespace std;


#define all(x) (x).begin(),(x).end()
#define sz(s) int((s).size())
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


#undef int

vector <string> split(const string& str, const char& del) {
  vector <string> ret;
  string temp;
  for (char ch: str) {
    if (ch != del) {
      temp += ch;
    }
    else {
      if(sz(temp) > 0) ret.emplace_back(temp);
      temp = "";
    }
  }
  if(sz(temp) > 0) ret.emplace_back(temp);
  return ret;
}

map<string, int> numberMap = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
    };


int isnewdig (string x, int idx) {
  string s = "";
  for (int i = idx; i < sz(x); ++i) {
    s += x[i];
    if (numberMap[s] > 0) {
      return numberMap[s];
    }
  }
  return 0;
}

int isnewdigrev (string x, int idx) {
  string s = "";
  for (int i = idx; i >= 0; --i) {
    s += x[i];
    string ts = s;
    reverse(s.begin(), s.end());
    if (numberMap[s] > 0) {
      return numberMap[s];
    }
    s = ts;
  }
  return 0;
}


int main () {
  freopen("in.txt", "r", stdin);
  string x;
  ll sm = 0;
  while (cin >> x) {
    ll f, l;
    rep(i, sz(x)) {
      if (isdigit(x[i])) {
        f = x [i] - 48;
        break;
      }
      ll ft = isnewdig(x, i);
      if (ft) {
        f = ft;
        break;
      }
    }
    for (int i = sz(x) - 1; i >= 0; --i) {
      if (isdigit(x[i])) {
        l = x [i] - 48;
        break;
      }
      ll lt = isnewdigrev(x, i);
      if (lt) {
        l = lt;
        break;
      }
    }
    sm += f*10 + l;
  }
  cout << sm << endl;
}





















