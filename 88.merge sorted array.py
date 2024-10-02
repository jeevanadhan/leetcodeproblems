class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # given num1 , num2 , m=3 for num1 , n=3 for num3
        # merging the sorted nums1 and nums2 in nums1
        index = m + n - 1
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
            else:
                nums1[index] = nums2[n - 1]
                n -= 1
            index -= 1

