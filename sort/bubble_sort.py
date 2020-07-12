'''
Bubble sort Example

 * input:[9, 8, 10, 5], then
 * [8, 9, 10, 5]
 * [8, 9, 5, 10]
 * [8, 5, 9, 10]
 * [5, 8, 9, 10] done.
'''


def sort(nums):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(sort([9, 8, 5, 10]))
print(sort([2, 9, 5, 1, 3]))
