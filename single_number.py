class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = dict()
        for i in nums:
            d[str(i)] = d.get(str(i), 0) + 1
        print(d)
        for ke_va in d.items():
            if ke_va[1] == 1:
                return ke_va[0]

sol = Solution()

print(sol.singleNumber([1]))