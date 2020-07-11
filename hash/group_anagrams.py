'''
* Problem No. : 49
* Problem Name: Group Anagrams
* Problem URL : https://leetcode.com/problems/group-anagrams/description/
* Date        : Oct 26 2017
* Author      :	Xian Lin
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
* meta        : tag-hash, tag-array-map, tag-bloomberg
'''


class Solution:
    def group_anagrams(self, strs):
        res = []
        if (len(strs) == 0):
            return res
        map = dict()
        for s in strs:
            key = ''.join(sorted(s))
            # map[key] = map.get(key, []).append(s)
            # Cannot use .append(s) cuz the append() for a list does not
            # return any value!!! NoneType
            map[key] = map.get(key, []) + [s]
        for key in map:
            res.append(map[key])
        return res


sol = Solution()
print(sol.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
