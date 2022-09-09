class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        total = 0
        comp = 0
        while right  < len(nums):
            total += nums[right]
            while nums[right]*(right - left + 1) > total + k and left < len(nums):
                total -= nums[left]
                left +=1

            if right - left + 1 > comp:
                comp = right - left + 1
            right +=1

        return comp
