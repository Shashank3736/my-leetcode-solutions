# Leetcode 23: Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
from typing import Optional
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            while lst:
                heap.append(lst.val)
                lst = lst.next
        heapq.heapify(heap)
        dummy = cur = ListNode(0)
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dummy.next
