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


map <string, vector <string>> g;
map <string, string> par;
map <string, ll> siz;
map <string, bool> vis;

//vector <vector <int>> v2;
//v2.resize(rows, vector<int>(cols, -1));

//vector<vector<vector<int> > > v3 (10, vector<vector<int> >(5, vector<int>(5)));

ll ans = 0;

void dfs (string u) {
  //  show(u)
  vis [u] = 1;
  for (auto v: g[u]) {
    if (!vis [v]) {
      dfs (v);
      //      show2 (u, v)
      siz [u] += siz [v];
    }
  }
  if (siz[u] <= 100000) {
    ans += siz[u];
  }
}



void solve () {
  DebugHelper dh;
  
  string s;
  vector <ll> v;
  vector <string> str;
  string curr_vertex = "0";
  
  while (getline(cin, s)) {
    vector <string> inp = split(s, ' ');
    string cmd = inp [0];
    
    if (cmd == "$") {
      // either $cd or $ls
      string cmd2 = inp [1];
      if (cmd2 == "cd") {
        string cmd3 = inp [2];
        if (cmd3 == "..") curr_vertex = par [curr_vertex];
        else { // ex: cd a
          cmd3 = curr_vertex + ">" + cmd3;
          par [cmd3] = curr_vertex;
          curr_vertex = cmd3;
        }
        
      } else if (cmd == "ls") {
        continue;
      }
      
    } else if (cmd == "dir") {
      // if not cd after $ then all are the result of ls
      string cmd2 = inp [1];
      cmd2 = curr_vertex + ">" + cmd2;
      par [cmd2] = curr_vertex;
      //      show2 (curr_vertex, cmd2)
      g [curr_vertex].push_back(cmd2);
      
    } else {
      //      show2 (curr_vertex, cmd)
      siz [curr_vertex] += stoll(cmd);
    }
    
  }
  
  show(siz["0>/"])
  
  dfs ("0>/");
  
  ll can = 40000000;
  ll now = siz["0>/"];
  ll diff = now - can;
  show2 (now, diff)
  
  vector <int> all_cnts;
  int curr = 0, ans2 = 0;
  
  for (auto [x, y]: siz) {
    all_cnts.push_back(y);
  }
  
  sort(all(all_cnts));
  
  for (auto cnt: all_cnts) {
    if (curr + cnt >= diff) {
      ans2 = cnt;
      break;
    }
  }
  
  dh.showVector(all_cnts);
  
  
  show(ans);
  show(ans2);
}


#undef int


int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
#endif
  solve();
}

