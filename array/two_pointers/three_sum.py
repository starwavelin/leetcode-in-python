class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myset = set()
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            target = 0 - nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    myset.add((nums[i], nums[j], nums[k]))
                    print(myset)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return list(myset)
    
    '''
    Pointer moving solution
    '''
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        i = 0
        while i < length - 2:
            target = 0 - nums[i]
            l = i + 1
            r = length - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < length-1:
                        l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            i += 1
            while nums[i] == nums[i-1] and i < length-2:
                i += 1
        return res