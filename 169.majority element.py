class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        for i in nums:
            m[i]=m.get(i,0)+1

            if m[i] > len(nums)/2:
                return i



