class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        len_nums = len(nums) - 1

        flag = False
        ind = 0
        while start <= len_nums and not flag:
            middle_len = (start + len_nums) // 2
           
            if nums[middle_len] == target:
                ind = middle_len
                
                flag = True
            elif nums[middle_len] > target:
                len_nums = middle_len - 1
               
                if nums[middle_len] > target and nums[middle_len - 1] < target:
                    
                    ind = middle_len 
                    
                    break

            elif nums[middle_len] < target:
                start = middle_len + 1

                if target > nums[-1]:
                    ind = len_nums + 1
                    break
               
        if ind < 0:
            return 0
        else:
            return ind
        


sol = Solution()

print(sol.searchInsert([1, 2, 5, 6], 7))