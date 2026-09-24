class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        known = set()

        for num in nums:
            known.add(num)

        if len(known) < len(nums):
            return True
        else:
            return False