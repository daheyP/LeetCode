class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   

        vDic = {}
        for i in range(len(nums)):
            if nums[i] in vDic:
                 return [vDic[nums[i]],i]
            vDic[target-nums[i]] = i
        return "Not Found"
    
s = Solution()
s.twoSum([2,7,11,15],9)
