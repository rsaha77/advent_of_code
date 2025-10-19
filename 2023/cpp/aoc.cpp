// headers
#ifndef LOCAL
#include <bits/stdc++.h>
#else
#include "header.h"
#include "debug.h"
#endif
using namespace std;


// others
#define all(x) (x).begin(),(x).end()
#define sz(s) int((s).size())
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define ru(i,a,b) for(int(i)=a; (i)<(b);++(i))
#define rd(i,a,b) for(int(i)=a; (i)>(b);--(i))
#define FASTIO istream::sync_with_stdio(0); cin.tie(0); cout.tie(0);


typedef long long int ll;
#define int ll
typedef pair <int,int> pii;
template <class T> inline T nxt () {T x; cin >> x; return x;}
template <class T> inline void ckmin (T& a, T b) {a = min (a, b);}
template <class T> inline void ckmax (T& a, T b) {a = max (a, b);}
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> bool ins(T a, T b, T c, T d) {return (0 <= a && a < c && 0 <= b && b < d);}


vector <string> split (const string& str, const char& del) {
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

void keep_alp_num_space (string& str) {
  // Keep alphanumeric characters and spaces
  str.erase(remove_if(str.begin(), str.end(), [](char c) {
    return !(isalnum(static_cast<unsigned char>(c)) or c == ' ');
  }), str.end());
}


void remove_chars (string& str, const string& charsToRemove) {
  str.erase(remove_if(str.begin(), str.end(), [&](char c) {
    return charsToRemove.find(c) != string::npos;
  }), str.end());
}

void remove_first_n (std::vector<std::string>& vec, size_t n) {
  ckmin (n, vec.size());
  vec.erase(vec.begin(), vec.begin() + n);
}


// variables
// const int MAX_N = 500;
// const int dir[4][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}};
// const int dir[8][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
// vector <bool> my_vector (MAX_N, false);
// vector <vector <bool> > my_2D_vector (MAX_N, vector<bool>(MAX_N, false));
// vector <vector <vector <bool> > > my_3D_vector (MAX_N, vector <vector<bool>>(MAX_N, vector<bool>(MAX_N, false)));



void solve () {
  DebugHelper dh;
  string line;

  int idx = 0, ans = 0;
  vector <string> v, myseeds;
  // map <int, bool> found_seed;
  map <int, int> seed_map;

  while (getline(cin, line)) {

    // cout << line << endl;

    if (line[sz(line)] != ':' and !isdigit (line[0])) {
      // get seeds
      v = split (line, ':');
      if (v[0] == "seeds") {
        myseeds = split (v[1], ' ');
        dh.showVector(myseeds);
        for (string x: myseeds) {
          int seed = stoll (x);
          seed_map [seed] = seed;
        }
      }

    } else if (line[sz(line)] == ':') {
      // calculate values and clear map
      // mp.clear();

    } else if (isdigit (line[0])) {
      v = split (line, ' ');
      int source = stoll (v[1]);
      int dest = stoll (v[0]);
      int tot = stoll (v[2]);
      show3 (dest, source, tot);
      rep (i, tot) {
        cout << source << " -> " << dest << endl;
        for (string x: myseeds) {
          int seed = stoll (x);
          if (seed == source) {
            seed_map [seed] = dest;
          }
        }
        source += 1;
        dest += 1;
      }

      myseeds.clear();

      for (auto& [x,y]: seed_map) {
        myseeds.push_back(to_string(y));
      }

      seed_map.clear ();
      for (string x: myseeds) {
        int seed = stoll (x);
        seed_map [seed] = seed;
      }

    }
  }

  for (auto& [x,y]: seed_map) {
    show2 (x, y);
  }

}


#undef int

int main () {
  FASTIO
  freopen("in.txt", "r", stdin);
  solve ();
}




























