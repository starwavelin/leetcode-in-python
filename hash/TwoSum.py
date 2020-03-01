'''
* Problem No. : 1
* Problem Name: Two Sum
* Problem URL : https://leetcode.com/problems/two-sum/description/
* Date        : Oct 18 2017
* Author      :	Xian Lin
* Notes       :
* 	Scenario:
* 		Given an array of integers, return indices of the two numbers such that they add up to a specific target.
* 	Assumption:
* 		1. If there are more than 1 solutions, return 1 solution is fine
* 		2. If there are no solutions, return [-1, -1]
	Example:
* 	Input: [33, -2, 14, 5, 4, 9] target 3
* 	Output: [1, 3]
* 	Data Structure and Alg:
* 		See Code Comments
* Complexity  :
* 	Time Complexity: O() -- See Code Comments
* 	Space Complexity: O() -- See Code Comments
*
* meta        : tag-array, tag-two-pointers, tag-sort, tag-hash
'''

from typing import List

class Solution1:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) < 2:
            return [-1, -1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution1()
# print(sol.two_sum([33, -2, 14, 5, 4, 9], 3)) # should print out [1, 3]
# print(sol.two_sum([3, 2, 4], 6)) # should print out [1, 2]


class Solution2:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) < 2:
            return [-1, -1]
        elems = []
        for i in range(len(nums)):
            elems.append((nums[i], i))
        elems.sort(key = lambda e: e[0])
        i = 0
        j = len(elems) - 1
        while (i < j):
            if (elems[i][0] + elems[j][0] == target):
                return [elems[i][1], elems[j][1]]
            elif (elems[i][0] + elems[j][0] < target):
                i += 1
            elif (elems[i][0] + elems[j][0] > target):
                j -= 1
        return [-1, -1]

sol = Solution2()
# print(sol.two_sum([33, -2, 14, 5, 4, 9], 3)) # should print out [1, 3]
# print(sol.two_sum([3, 2, 4], 6)) # should print out [1, 2]

class Solution3:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) < 2:
            return [-1, -1]
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return map[target - nums[i]], i
            map[nums[i]] = i
        return -1, -1

sol = Solution3()
print(sol.two_sum([33, -2, 14, 5, 4, 9], 3)) # should print out [1, 3]
print(sol.two_sum([3, 2, 4], 6)) # should print out [1, 2]
