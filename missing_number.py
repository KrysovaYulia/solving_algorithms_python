class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum([j for j in range(0, len(nums) + 1)]) - sum(nums)

sol = Solution()

print(sol.missingNumber([3,0,1]))