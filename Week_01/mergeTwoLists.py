class Solution:
    def mergeTwoLists(self, l1, l2):
        # 思路：递归解法，时间复杂度为O(n)，常熟级别，n为两个链表的总长度
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 思路：嵌套遍历两个链表，比较两个节点的值大小，进行拼接，时间复杂度为O(n*2)