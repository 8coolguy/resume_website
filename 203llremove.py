[200~# Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution:
            def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
                    if head:
                                while head and head.val ==val:
                                                head=head.next
                                                            if not head:
                                                                            return head
                                                                                        cur =head
                                                                                                    prev=cur
                                                                                                                while cur.next:
                                                                                                                                cur=cur.next
                                                                                                                                                if cur.val ==val:
                                                                                                                                                                    prev.next=cur.next
                                                                                                                                                                                    else:
                                                                                                                                                                                                        prev=cur
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
