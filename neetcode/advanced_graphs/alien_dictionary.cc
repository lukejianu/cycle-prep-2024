#include <algorithm>
#include <iostream>
#include <optional>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using Graph = std::unordered_map<char, std::unordered_set<char>>;

class Solution {
 public:
  std::string alienOrder(std::vector<std::string>& words) {
    auto pair = buildGraph(words);
    if (!pair.has_value()) return "";
    Graph graph = pair.value().first;
    std::unordered_map<char, int> indegree = pair.value().second;
    std::queue<char> q;
    std::string res;
    for (auto& node : indegree) {
      if (node.second == 0) {
        q.push(node.first);
      }
    }
    while (!q.empty()) {
      char curr = q.front();
      q.pop();
      res += curr;
      for (auto& out : graph[curr]) {
        indegree[out] -= 1;
        if (indegree[out] == 0) {
          q.push(out);
        }
      }
    }
    // Verify that all nodes have been visited.
    for (auto& v : indegree)
      if (v.second > 0) return "";

    return res;
  }

  std::optional<std::pair<Graph, std::unordered_map<char, int>>> buildGraph(
      std::vector<std::string>& words) {
    if (!words.size()) {
      return std::nullopt;
    }
    Graph graph;
    std::unordered_map<char, int> indegree;
    for (auto& word : words) {
      for (auto c : word) {
        indegree[c] = 0;
      }
    }
    for (int i = 0; i < words.size() - 1; ++i) {
      std::string w1 = words[i];
      std::string w2 = words[i + 1];
      int minLength = std::min(w1.length(), w2.length());
      // If the first is longer, yet the second is a substring of the first.
      if (w1.size() > w2.size() && w1.substr(0, minLength) == w2) {
        return std::nullopt;
      }
      for (int j = 0; j < minLength; ++j) {
        if (w1[j] != w2[j]) {
          auto& out = graph[w1[j]];
          if (out.count(w2[j]) == 0) {
            graph[w1[j]].insert(w2[j]);
            indegree[w2[j]]++;
          }
          break;
        }
      }
    }
    return std::make_pair(graph, indegree);
  }
};
