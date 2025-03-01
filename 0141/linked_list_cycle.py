class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        traversed = {}
        while head:
            if head in traversed:
                return True
            traversed[head] = True
            head = head.next
        return False
    
def form_ll(array, pos):
    head = ListNode(array[0])
    r_head = head
    node_at_pos = head
    for e in array[1:]:
        head.next = ListNode(e)
        head = head.next
    if pos == -1:
        return r_head
    for i in range(pos):
        node_at_pos = node_at_pos.next
    head.next = node_at_pos
    return r_head


if __name__ == "__main__":
    init_array = [3,2,0,-4]
    head = form_ll(init_array, -1)
    ptr = Solution()
    test_h = head
    for i in range(len(init_array)):
        print(f"{test_h.val} -> {test_h.next.val if test_h.next else None}")
        test_h = test_h.next
    print(ptr.hasCycle(head))
