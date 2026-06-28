class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        total = ( len(nums1) + len(nums2) )
        half = ( total ) // 2

        left, right = 0 , len(nums1)

        while left <= right :

            i = ( left + right ) // 2
            j = half - i

            if i > 0:
                a_left = nums1[i-1]
            else:
                a_left = float('-inf')

            if i < len(nums1):
                a_right = nums1[i]
            else:
                a_right = float('inf')

            #########################    
            if j > 0:
                b_left = nums2[j-1]
            else:
                b_left = float('-inf')


            if j < len(nums2):
                b_right = nums2[j]
            else:
                b_right = float('inf')



            

            if a_left <= b_right and b_left <= a_right:
                
                if total % 2:
                    return min(a_right, b_right)

                else:
                    return ( max(a_left, b_left) + min(a_right, b_right)) / 2



            elif a_left > b_right:
                right = i - 1

            else:
                left = i + 1
