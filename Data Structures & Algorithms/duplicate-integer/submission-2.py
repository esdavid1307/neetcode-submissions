class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known = set()

        for i in range(len(nums)):
            if nums[i] in known:
                return True
            known.add(nums[i])
        return False