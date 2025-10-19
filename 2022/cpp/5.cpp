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


//map <string, vector <string>> g;

//vector <vector <int>> v2;
//v2.resize(rows, vector<int>(cols, -1));

//vector<vector<vector<int> > > v3 (10, vector<vector<int> >(5, vector<int>(5)));



string solve () {
  string s;
  vector <ll> v;
  
  vector <string> str;
  str.resize(9);
  
  int cnt = 0;
  
  
  while (getline(cin, s)) {
    if (cnt < 9) {
      str [cnt++] = s;
      continue;
    }
    vector <string> x = split(s, ' ');
    int move = stoll (x[0]);
    int from = stoll (x[1]);
    int to = stoll (x[2]);
    
    vector <char> move_dir;
    rep (curr, move) {
      char to_move = str [from - 1].back();
      move_dir.push_back(to_move);
      str [from - 1].pop_back();
    }
    
    reverse(all(move_dir));
    
    for (char ch: move_dir) {
      str [to - 1].push_back(ch);
    }
  }
  
  string ans = "";
  rep (i, 9) {
    ans += str[i].back();
  }
  
  return ans;
  
}


#undef int


int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
#endif
  cout << solve() << endl;
}

