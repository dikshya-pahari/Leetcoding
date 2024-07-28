# 141. Linked List Cycle
# Category : Easy
# https://leetcode.com/problems/linked-list-cycle/

# Technique: we can use Hash set to keep all the visited node to detect that we are visiting the same node twice

# Floyd's Tortoise & Hare Technique 
# - Slow pointer shifts by 1
# - Fast pointer shifts by 2
# - At some point slow and fast pointer meets that proves there's a cycle

# Time complexity : O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return true
        return false