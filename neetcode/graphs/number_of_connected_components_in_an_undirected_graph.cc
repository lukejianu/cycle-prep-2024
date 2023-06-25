#include <iostream>
#include <unordered_set>
#include <vector>

struct DSU {
  std::vector<int> e;
  DSU(int n) { e = std::vector<int>(n, -1); };

  int find(int node) {
    if (e[node] < 0) {
      return node;
    }
    e[node] = find(e[node]);  // Path compression.
    return e[node];
  };

  bool sameSet(int x, int y) { return find(x) == find(y); }

  int size(int node) { return -find(node); }

  bool unite(int x, int y) {
    x = find(x), y = find(y);
    if (x == y) {
      return false;
    }
    // x should be longest chain.
    if (e[x] > e[y]) {
      std::swap(x, y);
    }
    e[x] += e[y];
    e[y] = x;
    return true;
  };
};

class Solution {
 public:
  int countComponents(int n, std::vector<std::vector<int>>& edges) {
    return countComponentsUF(n, edges);
  }

  int countComponentsUF(int n, std::vector<std::vector<int>>& edges) {
    DSU uf(n);
    int components = n;

    for (auto& edge : edges) {
      if (uf.unite(edge[0], edge[1])) {
        components -= 1;
      }
    }
    return components;
  }

  int countComponentsDFS(int n, std::vector<std::vector<int>>& edges) {
    std::vector<std::vector<int>> graph = buildGraph(n, edges);
    std::vector<int> components(n, -1);
    for (int node = 0; node < n; ++node) {
      if (components[node] == -1) {
        dfs(node, node, components, graph);
      }
    }
    return std::unordered_set<int>(components.begin(), components.end()).size();
  }

  void dfs(const int node, const int parent, std::vector<int>& components,
           const std::vector<std::vector<int>>& graph) {
    components[node] = parent;
    for (auto& out : graph[node]) {
      if (components[out] == -1) {
        dfs(out, parent, components, graph);
      }
    }
  }

  std::vector<std::vector<int>> buildGraph(
      const int n, const std::vector<std::vector<int>>& edges) {
    std::vector<std::vector<int>> graph(n);
    for (const auto& edge : edges) {
      graph[edge[0]].push_back(edge[1]);
      graph[edge[1]].push_back(edge[0]);
    }
    return graph;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> v;
  s.countComponents(0, v);
}
