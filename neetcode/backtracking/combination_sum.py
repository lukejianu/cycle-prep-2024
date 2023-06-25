# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 
        
        def dfs(i, chosen, curr_sum): 
            if curr_sum == target:
                result.append(chosen)
                return

            if curr_sum > target or i >= len(candidates):
                return

            dfs(i, chosen + [candidates[i]], curr_sum + candidates[i])
            dfs(i + 1, chosen, curr_sum)
        
        dfs(0, [], 0)
        return result
