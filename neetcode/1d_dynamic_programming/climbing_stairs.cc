#include <unordered_map>
#include <vector>

class Solution {
 public:
  int climbStairs(int n) {
    // std::unordered_map<int, int> memo;
    return bottomUpOptimized(n);
  }

  int bottomUp(int n) {
    // table[i] = distinct ways to reach stair n from stair i.
    if (n == 1) return 1;
    std::vector<int> table(n + 1);
    table[n - 1] = 1;
    table[n - 2] = 2;
    for (int i = n - 3; i >= 0; --i) {
      table[i] = table[i + 1] + table[i + 2];
    }
    return table[0];
  }

  int bottomUpOptimized(int n) {
    if (n == 1) return 1;
    int first = 1;
    int second = 2;
    for (int i = 3; i <= n; ++i) {
      int third = first + second;
      first = second;
      second = third;
    }
    return second;
  }

  int topDown(int n, std::unordered_map<int, int>& memo) {
    if (n == 0) return 1;
    if (n == 1) return 1;
    auto steps = memo.find(n);
    if (steps == memo.end()) {
      memo[n] = topDown(n - 1, memo) + topDown(n - 2, memo);
    }
    return memo[n];
  }
};
