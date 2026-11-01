class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_frequency = {}

        for num in nums:
            if num not in nums_frequency:
                nums_frequency[num] = 1
            else:
                nums_frequency[num] = nums_frequency[num] + 1
        
        for key in nums_frequency:
            if nums_frequency[key] >= 2:
                return True
        return False

