class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            ans.append(count)
        return ans
