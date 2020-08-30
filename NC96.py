# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 the head
# @return bool布尔型
# class Solution:
#     def isPail(self , head ):
#         val_list = []
#         cur = head
#         length = 0
#         while(cur):
#             val_list.append(cur.val)
#             cur = cur.next
#             length += 1
            
#         for i in range(length // 2):
#             if val_list[i] != val_list[length-i-1]:
#                 return False
#         return True

s=input()
s=s[1:-1]
l = s[::-1]
if s==l:
    print('true')
else:
    print('false')
