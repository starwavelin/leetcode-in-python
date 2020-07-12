'''
Selection sort Example

 * input:[2, 9, 5, 1, 3], then
 * [1, 9, 5, 2, 3]
 * [1, 2, 5, 9, 3]
 * [1, 2, 3, 9, 5]
 * [1, 2, 3, 5, 9] done.
'''


def sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


print(sort([2, 9, 5, 1, 3]))
print(sort([22, 18, 1, 13, 15, 6, 17, 4, 2, 9]))
