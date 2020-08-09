'''
Explanation Blog Article:
http://starwavelin.io/2019/10/19/NLC-9-Quick-Sort-Fast-Slow-Pointers/
'''


class Solution:
    def sort(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if (left < right):
            par_index = self.partition(nums, left, right)
            self.quick_sort(nums, left, par_index - 1)
            self.quick_sort(nums, par_index + 1, right)

    def partition(self, nums, left, right):
        pivot = left
        i = pivot + 1
        for j in range(i, right + 1):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        if pivot != i-1:
            nums[pivot], nums[i-1] = nums[i-1], nums[pivot]
        return i - 1


sol = Solution()
print(sol.sort([3, 5, 1, 2, 7, 6, 4]))
print(sol.sort([22, 18, 1, 13, 15, 6, 17, 4, 2, 9]))
