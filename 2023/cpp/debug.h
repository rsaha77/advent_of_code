#ifndef debug_h
#define debug_h

#include "iostream"
#include "vector"
using namespace std;

#define pn puts("");
#define sz(x) int((x).size())
#define rep(i, n) for(int(i)=0; (i)<(n);++(i))
#define show(x) cout<<#x<<": "<<(x)<<"\n";
#define show2(x,y) cout<<#x<<": "<<(x)<<" | "<<#y<<": "<<(y)<< "\n";
#define show3(x,y,z) cout<<#x<<": "<<(x)<<" | "<<#y<<": "<<(y)<<" | "<<#z<<": "<<(z)<<"\n";
#define show4(x,y,z,p) cout<<#x<<": "<<(x)<<" | "<<#y<<": "<<(y)<<" | "<<#z<<": "<<(z)<<" | "<<#p<<": "<<(p)<<"\n";

struct DebugHelper {
  template <class T>
  void showVector(vector<T>& v) {
    cout << "[";
    rep(i, sz(v)) {
      cout << '\'' << v[i] << '\'';
      if (i < sz(v) - 1) cout << ", ";
    }
    puts("]");
  }
  
  template <class T>
  void show2DVector(vector<vector<T>>& v) {
    puts("");
    puts("");
    rep(i, sz(v)) {
      cout << "[";
      rep(j, sz(v[i])) {
        cout << v[i][j];
        if (j < sz(v[i])-1) cout << " -> ";
      }
      puts("]");
    }
    puts("");
    puts("");
  }
};


template <class T>
void print (T a) {
  cout << a << endl;
}

template <class T>
void print (T a, T b) {
  cout << a << " " << b << endl;
}

template <class T>
void print (T a, T b, T c) {
  cout << a << " " << b << " " << c << endl;
}


template <class T>
void print (T a, T b, T c, T d) {
  cout << a << " " << b << " " << c << " " << d << endl;
}

#endif /* debug_h */
