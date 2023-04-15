'''
* Problem No. : NLC 1
* Problem Name: Longest Uniform Substring
* Problem URL :
* Date        : Jan 3 2017
* Author      :	Xian Lin
* Notes       :
* 	Scenario:
* 		Also known as Longest Uniform Substring.
* 		Given a string, find the starting index and the length of the longest
*   substring with repeating characters.
* 	Assumption:
* 		1. Can input be an empty string? Yes, then its index will be -1 and
*   length will be 0
*	Example:
* 	Input/Output:
* 		Given "aaoooookk", the answer is int[]{2, 5}.
* 		ooooo contributes to the answer with starting index 2 and length 5.
* 	Data Structure and Alg:
* 		see code comments
* Complexity  :
* 	Time Complexity: O() -- see code comments
* 	Space Complexity: O() -- see code comments
*
* meta        : tag-string, tag-two-pointers
'''


class Solution:
    def lus(self, str):
        if (len(str) == 0):
            return (-1, 0)
        max_start_index = 0
        cur_start_index = max_start_index
        max_len = 1
        cur_len = max_len
        for i in range(1, len(str)):
            if (str[i - 1] == str[i]):
                cur_len += 1
            else:
                cur_len = 1
                cur_start_index = i
            if (cur_len > max_len):
                max_len = cur_len
                if (max_start_index != cur_start_index):
                    max_start_index = cur_start_index
        return (max_start_index, max_len)


sol = Solution()
print(sol.lus(''))  # should print out (-1, 0)
print(sol.lus('Y'))  # should print out (0, 1)
print(sol.lus('zzbbbccd'))  # should print out (2, 3)
print(sol.lus('kyx88888rtttt5'))  # should print out (3, 5)
