'''
Insertion sort Example

 * input:[2, 9, 5, 1, 3], then
 * [1, 2, 9, 5, 3]
 * [1, 2, 3, 9, 5]
 * [1, 2, 3, 5, 9] done.
'''


def sort(nums):
    for i in range(1, len(nums)):
        j = i
        cur = nums[j]
        while (j > 0 and nums[j - 1] > cur):
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = cur
    return nums


print(sort([2, 9, 5, 1, 3]))
print(sort([22, 18, 1, 13, 15, 6, 17, 4, 2, 9]))
