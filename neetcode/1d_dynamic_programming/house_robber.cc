#include <unordered_map>
#include <vector>

class Solution {
 public:
  int rob(std::vector<int>& nums) {
    // int n = nums.size();
    // std::unordered_map<int, int> memo;
    return bottomUpOptimized(nums);
    //  return std::max(topDown(0, n, nums, memo), topDown(1, n, nums, memo));
  }

  int topDown(int i, int n, const std::vector<int>& nums,
              std::unordered_map<int, int>& memo) {
    if (i >= n) return 0;
    auto money = memo.find(i);
    if (money == memo.end()) {
      memo[i] = std::max(nums[i] + topDown(i + 2, n, nums, memo),
                         topDown(i + 1, n, nums, memo));
    }
    return memo[i];
  }

  int bottomUp(const std::vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    // table[i] = optimal robbed from nums[i:n]
    std::vector<int> table(n + 1);
    table[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
      table[i] = std::max(nums[i] + table[i + 2], table[i + 1]);
    }
    return table[0];
  }

  int bottomUpOptimized(const std::vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    int neigh = nums[n - 1]; int nextNeigh = 0;
    for (int i = n - 2; i >= 0; --i) {
      int temp = std::max(nums[i] + nextNeigh, neigh);
      nextNeigh = neigh;
      neigh = temp;
    }
    return neigh;
  }
};
