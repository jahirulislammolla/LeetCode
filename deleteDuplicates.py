class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        while curr:
            while curr.next and curr.val==curr.next.val:
                curr.next=curr.next.next
            curr=curr.next
        return head
            
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    var cur=head
    while (cur)
        {
            while(cur.next && cur.val==cur.next.val)
                {
                    cur.next=cur.next.next;
                }
            cur=cur.next;
        }
    return head;
};
