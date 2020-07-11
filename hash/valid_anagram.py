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
