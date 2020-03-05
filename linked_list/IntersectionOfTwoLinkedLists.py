'''
* Problem No. : 160
* Problem Name: Intersection of Two Linked Lists
* Problem URL : https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
* Date        : March 04 2020
* Author      :	Xian Lin
* Notes       :
*
* meta        : tag-linked-list
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None;
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)
        if lenA > lenB:
            for i in range(0, lenA - lenB):
                headA = headA.next
        else:
            for i in range(0, lenB - lenA):
                headB = headB.next
        while (headA is not None and headB is not None and headA is not headB):
            headA = headA.next
            headB = headB.next
        return headA if (headA is not None and headB is not None) else None

    def get_length(self, head: ListNode):
        count = 0
        while (head != None):
            count += 1
            head = head.next
        return count
