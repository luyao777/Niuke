# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head , k ):
        def reverse(a,b):
            pre = None
            cur = a
            while cur != b:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            return pre
         
        a,b = head,head
        for i in range(k):
            if not b: return head
            b = b.next
        newHead = reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return newHead
