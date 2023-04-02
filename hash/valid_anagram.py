'''
* Problem No. : 242
* Problem Name: Valid Anagram
* Problem URL : https://leetcode.com/problems/valid-anagram/description/
* Date        : Oct 26 2017
* Author      :	Xian Lin
* Notes       :
* 	Scenario:
* 		@needOrganize
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


def valid_anagram(s, t):
    if (len(s) != len(t)):
        return False
    map = [0 for i in range(26)]
    for i in range(len(s)):
        map[ord(s[i]) - ord('a')] += 1
    for i in range(len(t)):
        map[ord(t[i]) - ord('a')] -= 1
        if (map[ord(t[i]) - ord('a')] < 0):
            return False
    return True


print(valid_anagram('', ''))  # should be True
print(valid_anagram('k', 'k'))  # should be True
print(valid_anagram('b', 'k'))  # should be False
print(valid_anagram('abc', 'bca'))  # should be True
print(valid_anagram('abd', 'bca'))  # should be False


# array map solution
def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    array_map = [0] * 26
    for i in range(len(s)):
        array_map[ord(s[i]) - 97] += 1
    for i in range(len(t)):
        array_map[ord(t[i]) - 97] -= 1
        if (array_map[ord(t[i]) - 97] < 0):
            return False
    return True

# array map solution 优化looping, python允许直接通过char去loop一个string

def is_anagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    array_map = [0] * 26
    for char in s:
        array_map[ord(char) - 97] += 1
    for char in t:
        array_map[ord(char) - 97] -= 1
        if (array_map[ord(char) - 97] < 0):
            return False
    return True

# map solution
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map = {}
    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1
    for i in range(len(t)):
        if t[i] not in map or map[t[i]] == 0:
            return False
        map[t[i]] = map.get(t[i]) - 1
    return True