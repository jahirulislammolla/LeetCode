class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        m=head
        pre=None
        while m:
            c=0
            while m.val==val:
                c=1
                if not m.next:
                    m=None
                    break
                m=m.next
            if c==1 and pre==None:
                head=m
            if c==1 and pre!=None:
                pre.next=m
            pre=m
            if m:
                m=m.next
        return head
