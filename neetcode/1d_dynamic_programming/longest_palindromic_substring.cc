#include <string>
#include <vector>

using Memo = std::vector<std::vector<int>>;

struct Longest {
  int l;
  int r;
};

class Solution {
 public:
  std::string longestPalindrome(std::string s) {
    Memo memo(s.size(), std::vector<int>(s.size()));
  }
};
