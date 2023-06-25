#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

enum class NodeState { Unvisited, Visiting, Visited };

class Solution {
 public:
  bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
    return canFinishKahns(numCourses, prerequisites);
  }

  bool canFinishDFS(int numCourses,
                    const std::vector<std::vector<int>>& prerequisites) {
    std::vector<std::vector<int>> graph = buildGraph(numCourses, prerequisites);
    std::vector<NodeState> visiting(numCourses, NodeState::Unvisited);
    for (int course = 0; course < numCourses; ++course) {
      if (dfs(course, visiting, graph)) {
        return false;
      }
    }
    return true;
  }

  bool canFinishKahns(int numCourses,
                      const std::vector<std::vector<int>>& prerequisites) {
    std::vector<std::vector<int>> graph(numCourses);
    std::vector<int> indegree(numCourses);
    for (const auto& prereq : prerequisites) {
      graph[prereq[1]].push_back(prereq[0]);
      indegree[prereq[0]] += 1;
    }
    std::queue<int> q;
    for (int course = 0; course < numCourses; ++course) {
      if (indegree[course] == 0) {
        q.push(course);
      }
    }
    while (!q.empty()) {
      int course = q.front();
      q.pop();
      numCourses -= 1;
      for (const int out : graph[course]) {
        if (--indegree[out] == 0) {
          q.push(out);
        }
      }
    }
    return numCourses == 0;  // If every node was added/removed from the queue.
  }

  // Determines if there is a cycle in the given graph.
  bool dfs(const int& node, std::vector<NodeState>& visiting,
           const std::vector<std::vector<int>>& graph) {
    if (visiting[node] == NodeState::Visiting) {
      return true;
    }
    // Early return.
    if (visiting[node] == NodeState::Visited) {
      return false;
    }
    visiting[node] = NodeState::Visiting;
    for (const int outNeighbor : graph[node]) {
      if (dfs(outNeighbor, visiting, graph)) {
        return true;
      }
    }
    visiting[node] = NodeState::Visited;
    return false;
  }

  // Builds an adjacency list representation of a graph.
  std::vector<std::vector<int>> buildGraph(
      const int& courses, const std::vector<std::vector<int>>& prereqs) {
    std::vector<std::vector<int>> graph(courses);
    for (auto& prereq : prereqs) {
      graph[prereq[0]].push_back(prereq[1]);
    }
    return graph;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> prereqs{{0, 1}, {2, 3}, {0, 5}};
  std::vector<std::vector<int>> expected = {{1, 5}, {}, {3}};
  assert(s.buildGraph(3, prereqs) == expected);
  std::cout << "All tests pass!" << std::endl;
}
