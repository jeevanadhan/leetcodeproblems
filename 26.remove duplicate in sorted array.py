class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first value always be unique so starting pointer at second value
        #left pointer
        l=1
        #right pointer
        r=1
        while r<len(nums):
            #checking if the current right pointer not equal to previous right pointer
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                #if equal assign r to left pointer then move left and right pointer to right
                l+=1
                r+=1
            else:
                r+=1
        return l