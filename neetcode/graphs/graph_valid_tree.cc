#include <vector>

struct DSU {
  std::vector<int> e;
  DSU(int n) { e = std::vector(n, -1); }

  int get(int x) {
    if (e[x] < 0) {
      return x;
    }
    e[x] = get(e[x]);
    return e[x];
  }

  int size(int x) { return -e[get(x)]; }

  // Unites the two disjoint sets, returning true if were not disjoint (lol).
  bool unite(int x, int y) {
    x = get(x);
    y = get(y);
    if (x == y) {
      return false;
    }
    if (e[x] > e[y]) {
      std::swap(x, y);
    }
    e[x] += e[y];
    e[y] = x;
    return true;
  }
};

class Solution {
 public:
  bool validTree(int n, std::vector<std::vector<int>>& edges) {
    DSU dsu(n);
    for (auto& edge : edges) {
      if (!dsu.unite(edge[0], edge[1])) {
        return false;
      }
    }
    return dsu.size(0) == n;
  }
};
