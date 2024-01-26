class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list_node(l):
    if not l.next:
        print("")
    else:
        print_list_node(l.next)
    print(l.val, end='')


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0)
        if sum_val > 9:
            if l1 and l1.next:
                l1.next.val += sum_val // 10
            else:
                l1.next = ListNode(sum_val // 10)
        if not l1 and not l2:
            if sum_val > 0:
                return ListNode(sum_val % 10)
            else:
                return None
        return ListNode(sum_val % 10, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None))

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print_list_node(l1)
print_list_node(l2)
print_list_node(Solution().addTwoNumbers(l1,l2))