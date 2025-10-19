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
#define rd(i,a,b) for(int(i)=a; (i)>=(b);--(i))
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
template <class T> void resize(vector <vector <T>>& v, int M, int N, T val) {v.resize (M, vector<T> (N, val));}

const int MAX_N = 1000;
const int MID_N = 500;

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


DebugHelper dh;
//const int dir[8][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
//vector<vector<vector<bool>>> knot(MAX_N, vector <vector<bool>>(MAX_N, vector<bool>(MAX_N, false)));
//int prev_hr = MID_N, prev_hc = MID_N;


void make_move (const int hr, const int hc, int& tr, int& tc) {
  if (hr != tr and hc != tc and (abs (hr - tr) + abs (hc - tc) > 2)) {
    // move diag
    // (== 3) instead of (> 2) will give wrong ans for part 2
    if (hr < tr) tr -= 1; else tr += 1;
    if (hc < tc) tc -= 1; else tc += 1;
  }
  else if (hr == tr and abs (hc - tc) > 1) tc = min (hc, tc) + 1;
  else if (hc == tc and abs (hr - tr) > 1) tr = min (hr, tr) + 1;
}


void solve () {
  
  map <string, vector <int>> DIR;
  DIR ["R"] = {0, 1};
  DIR ["L"] = {0, -1};
  DIR ["U"] = {-1, 0};
  DIR ["D"] = {1, 0};

  string s;
  
  int hr = MID_N, hc = MID_N;
  vector <vector <int>> TR (10, vector <int> (2));
  vector <vector <int>> TC (10, vector <int> (2));
  
  vector<vector<vector<bool>>> tail (10, vector<vector<bool>>(MAX_N, vector <bool> (MAX_N, false)));
  rep (i, 9) {
    tail [i][MID_N][MID_N] = true;
    TR [i][0] = MID_N;
    TR [i][1] = MID_N;
    TC [i][0] = MID_N;
    TC [i][1] = MID_N;
  }
  
  
  while (getline(cin, s)) {
    vector line = split(s, ' ');
    string dir = line [0]; int moves = stoll(line[1]);
    while (moves--) {
      hr += DIR [dir][0];
      hc += DIR [dir][1];
      int r = hr;
      int c = hc;
      rep (i, 9) {
        int tr = TR [i][0];
        int tc = TR [i][1];
        make_move (r, c, tr, tc);
        TR [i][0] = tr;
        TR [i][1] = tc;
        tail [i][tr][tc] = true;
        r = tr;
        c = tc;
      }
    }
  }
  
  int ans = 0;
  
  rep (i,MAX_N)
    rep (j, MAX_N)
      if (tail [8][i][j])
        ans += 1;
  
  show(ans);
}


#undef int


int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
#endif
  solve();
}

