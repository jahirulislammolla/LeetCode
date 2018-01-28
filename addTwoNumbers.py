# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x,q=[],0
        while l1:
            if l2:
                p=(l1.val+l2.val)+q
                q=p//10
                l2=l2.next
            else:
                p=l1.val+q
                q=p//10
            x.append(p%10)
            l1=l1.next
            print(q)
        while l2:
            if l1:
                p=l1.val+l2.val+q
                q=p//10
                l1=l1.next
            else:
                p=l2.val+q
                q=p//10
            x.append(p%10)
            l2=l2.next
        if q==1:
            x.append(1)
        return x
