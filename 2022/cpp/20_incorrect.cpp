#ifndef LOCAL
#include <bits/stdc++.h>
#else
#include "header.h"
#include "debug.h"
#endif
using namespace std;


#define all(x) (x).begin(),(x).end()
#define sz(s) int((s).size())
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define ru(i,a,b) for(int(i)=a; (i)<(b);++(i))
#define FASTIO istream::sync_with_stdio(0); cin.tie(0); cout.tie(0);


typedef long long int ll;
#define int ll
typedef pair <int,int> pii;
template <class T> inline T nxt () {T x; cin >> x; return x;}
template <class T> inline void ckmin (T& a, T b) {a = min (a, b);}
template <class T> inline void ckmax (T& a, T b) {a = max (a, b);}
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> bool ins(T a, T b, T c, T d) {return (0 <= a && a < c && 0 <= b && b < d);}


// sublime: ctrl+shft+D = duplicate line
// get max of more than 2 elements => max({a, b, c});


// const int MAX_N = 1000;
// const int dir[4][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}};
// const int dir[8][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
// vector <bool> my_vector (MAX_N, false);
// vector <vector <bool> > my_2D_vector (MAX_N, vector<bool>(MAX_N, false));
// vector <vector <vector <bool> > > my_3D_vector (MAX_N, vector <vector<bool>>(MAX_N, vector<bool>(MAX_N, false)));



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

map <int, int> pos_original_to_new;
int N;

void move (vector <pii>& nums, int pos, int tot) {
  // show2(pos, tot)
  N = sz (nums);
  int npos = pos;
  // tot = abs (tot);
  if (tot < 0) {
    tot %= (N-1);
    tot = N - 1 + tot;
  }
  // show(tot)
  while (tot--) {
    npos += 1;
    npos %= N;
    // show2 (pos, npos)
    if (pos == N-1 and npos == 0) {
      pii last_num = nums [N - 1];
      for (int i = N-2; i >= 1; i--) {
        nums [i + 1] = nums [i];
        pos_original_to_new [nums[i + 1].ss] = i + 1;
      }
      nums [1] = last_num;
      pos_original_to_new [nums[N - 1].ss] = 1;
      // for (auto num: nums) {
      //   cout << num.ff << "," << num.ss << "  ";
      // }
      // pn
      pos = npos = 1;
      continue;
    }
    pos_original_to_new [nums[npos].ss] = pos;
    pos_original_to_new [nums[pos].ss] = npos;
    swap (nums [pos], nums [npos]);
    pos = npos;
  }
}

void solve () {
  DebugHelper dh;
  string line;
  int ans = 0;
  int ctr = 0;
  vector <pair <int, int>> nums;
  while (getline(cin, line)) {
    // keep_alp_num_space (line);
    // remove_chars (line, ",;....");
    // vector <string> words = split(line, ' ');
    int num = stoll (line);
    nums.push_back({num, ctr});
    pos_original_to_new [ctr] = ctr;
    ++ctr;
  }

  const vector <pii> ori = nums;

  // for (auto num: nums) {
  //   cout << num.ff << "," << num.ss << "  ";
  // }
  // pn

  int idx = -1;
  rep (i, sz(ori)) {
    // show(i)
    if (ori [i].ff == 0) {
      idx = i;
      continue;
    }
    move (nums, pos_original_to_new [i], ori [i].ff);
    // for (auto num: nums) {
    //   cout << num.ff << "," << num.ss << "  ";
    // }
    // pn
    // pn
  }


  ctr = 1;
  while (ctr <= 3000) {
    if (ctr and ctr % 1000 == 0) {
      // show2(idx, nums [idx].ff)
      ans += nums [idx].ff;
    }
    idx += 1;
    idx %= N;
    ctr += 1;
  }

  
  cout << ans << endl;
}


#undef int

int main () {
  FASTIO
  freopen("in.txt", "r", stdin);
  solve ();
}



























































