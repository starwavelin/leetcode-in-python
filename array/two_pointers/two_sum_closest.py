'''
* Problem No. :
* Problem Name: Two Sum Closest
* Problem URL : 
* Date        : Apr 7, 2023
* Author      :	Codingbro
* Notes       :
* 	Scenario:
*
* 	Assumption:
*
*	Example:
* 	Input/Output:
*
* 	Data Structure and Alg:
* 		See solutions in the code comments
* Complexity  :
* 	Time Complexity: See solutions in the code comments
* 	Space Complexity: See solutions in the code comments
*
* meta        : tag-sort, tag-two-pointers
'''

class Solution:
    def closest_sum(self, nums, target):
        nums.sort()
        # print(nums)
        length = len(nums)
        sum = nums[0] + nums[length-1]
        diff = abs(sum-target)
        i = 0
        j = length-1
        while i < j:
            local_sum = nums[i] + nums[j]
            local_diff = abs(local_sum - target)
            if local_diff < diff:
                diff = local_diff
                sum = local_sum
            if local_sum <= target:
                i += 1
            else:
                j -= 1
        return sum


sol = Solution()
print(sol.closest_sum([14, 5, -1, 7, 9], 11))  # should print 12
print(sol.closest_sum([6, 37, -8, -12, 25], 14))  # should print 13