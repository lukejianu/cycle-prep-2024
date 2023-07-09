#include <unordered_map>
#include <vector>

class Solution {
 public:
  int rob(std::vector<int>& nums) { return bottomUpOptimized(nums); }

  int topDown(std::vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) {
      return *std::max_element(nums.begin(), nums.end());
    }
    std::unordered_map<int, int> memo1;
    std::unordered_map<int, int> memo2;
    return std::max(topDownHelper(0, n - 1, nums, memo1),
                    topDownHelper(1, n, nums, memo2));
  }

  int topDownHelper(int i, int n, std::vector<int>& nums,
                    std::unordered_map<int, int>& memo) {
    if (i >= n) {
      return 0;
    }
    auto money = memo.find(i);
    if (money == memo.end()) {
      memo[i] = std::max(nums[i] + topDownHelper(i + 2, n, nums, memo),
                         topDownHelper(i + 1, n, nums, memo));
    }
    return memo[i];
  }

  int bottomUp(std::vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    return std::max(bottomUpHelper(0, n - 1, nums), bottomUpHelper(1, n, nums));
  }

  int bottomUpHelper(int start, int n, std::vector<int>& nums) {
    // table[i] = optimal money from nums[i:n]
    std::vector<int> table(n + 1);
    table[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= start; --i) {
      table[i] = std::max(nums[i] + table[i + 2], table[i + 1]);
    }
    return table[start];
  }

  int bottomUpOptimized(std::vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    return std::max(bottomUpOptimizedHelper(0, n - 1, nums), bottomUpOptimizedHelper(1, n, nums));
  }

  int bottomUpOptimizedHelper(int start, int n, std::vector<int>& nums) {
    int neigh = nums[n - 1], nextNeigh = 0;
    for (int i = n - 2; i >= start; --i) {
      int temp = std::max(nums[i] + nextNeigh, neigh);
      nextNeigh = neigh;
      neigh = temp;
    }
    return neigh;
  }
};
