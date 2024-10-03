class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #left pointer
        j = 0
        for i in range(len(nums)):
            #adding except val and counting no of elements except val
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j