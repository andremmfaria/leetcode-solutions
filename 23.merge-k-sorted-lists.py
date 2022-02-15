#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes_list = []

        if not lists: return None
        else:
            for index in range(len(lists)):
                temp: List[int] = []
                def get_val(node: Optional[ListNode]):
                    if node:
                        temp.append(node.val)
                        get_val(node.next)
                get_val(lists[index])
                nodes_list += temp

        nodes_list.sort()

        def create_node(nodes_list: List[int]) -> Optional[ListNode]:
            if not nodes_list: return None
            else:
                node = ListNode(nodes_list[0])
                node.next = create_node(nodes_list[1:])
                return node

        return create_node(nodes_list)

        
# @lc code=end

