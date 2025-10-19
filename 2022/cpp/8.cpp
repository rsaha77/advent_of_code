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
#define rd(i,a,b) for(int(i)=a; (i)>(b);--(i))
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

DebugHelper dh;
void solve_part_1(int R, int C, vector <vector <int>> v) {
  vector <vector <int>> cnt (R, vector<int> (C, 0));
  
  // down
  rep (c, C) {
    int mx = -1;
    rep (r, R) {
      if (v [r][c] > mx) {
        cnt [r][c] += 1;
      }
      ckmax (mx, v[r][c]);
    }
  }
  
  // up
  rep (c, C) {
    int mx = -1;
    rd (r, R-1, -1) {
      if (v [r][c] > mx) {
        cnt [r][c] += 1;
      }
      ckmax (mx, v[r][c]);
    }
  }
  
  // right
  rep (r, R) {
    int mx = -1;
    rep (c, C) {
      if (v [r][c] > mx) {
        cnt [r][c] += 1;
      }
      ckmax (mx, v[r][c]);
    }
  }
  
  
  // left
  rep (r, R) {
    int mx = -1;
    rd (c, C-1, -1) {
      if (v [r][c] > mx) {
        cnt [r][c] += 1;
      }
      ckmax (mx, v[r][c]);
    }
  }
  
  int ans = 0;
  rep(r,R) rep(c,C) {
    if (cnt [r][c]) {
      ans += 1;
    }
  }
  
  cout << "Part 1: " << ans << endl;
}

void solve_part_2(int R, int C, vector<vector<int>> v) {
  vector <vector <int>> cnt (R, vector<int> (C, 1));
  
  rep (r, R) {
    rep (c, C) {
      
      int now = v[r][c], curr_cnt;
      
      // down
      curr_cnt = 0;
      rep(idx, R) {
        if (idx > r) {
          curr_cnt += 1;
          if (v[idx][c] >= now) {
            break;
          }
        }
      }
      cnt [r][c] *= curr_cnt;
      
      
      // up
      curr_cnt = 0;
      rd (idx, R-1, -1) {
        if (idx < r) {
          curr_cnt += 1;
          if (v[idx][c] >= now) {
            break;
          }
        }
      }
      cnt [r][c] *= curr_cnt;
      
      // right
      curr_cnt = 0;
      rep (idx, C) {
        if (idx > c) {
          curr_cnt += 1;
          if (v[r][idx] >= now) {
            break;
          }
        }
      }
      cnt [r][c] *= curr_cnt;
      
      // left
      curr_cnt = 0;
      rd (idx, C-1, -1) {
        if (idx < c) {
          curr_cnt += 1;
          if (v[r][idx] >= now) {
            break;
          }
        }
      }
      cnt [r][c] *= curr_cnt;
    }
  }
  
  int ans = 0;
  rep(r, R) rep(c, C) {
    ckmax(ans, cnt[r][c]);
  }
  
  cout << "Part 2: " << ans << endl;
}

void solve () {
  string s;
  vector <string> str;
  
  while (getline(cin, s)) {
    str.push_back(s);
  }
  
  int R = sz(str);
  int C = sz(str[0]);
  
  vector <vector <int>> v (R, vector<int> (C));
  rep(i,R) rep(j,C) v[i][j] = str[i][j]-48;
  
  solve_part_1(R, C, v);
  solve_part_2(R, C, v);
}


#undef int


int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
#endif
  solve();
}

