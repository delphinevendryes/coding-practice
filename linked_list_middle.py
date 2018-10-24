'''
Given a singly linked list, find middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then output should be 3.
If there are even nodes, then there would be two middle nodes,
we need to print second middle element.
For example, if given linked list is 1->2->3->4->5->6 then output should be 4.
'''

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, *args, **kwargs):
        values = kwargs.get('values', None)
        N = len(values)
        for i in range(N):
            j = N - i - 1
            if i == 0:
                n = Node(values[j])
            else:
                n = Node(values[j], n)
        self.head = n

    def __len__(self):
        h = self.head
        count = 0
        while (h != None) :
            h = h.next
            count += 1
        return count

    def __repr__(self):
        h = self.head
        s = str()
        i = 0
        while h:
            if i != 0:
                s += ' -> '
            s += str(h.val)
            h = h.next
            i += 1
        return s

    def addAtBeginning(self, element):
        n = Node(element, self.head)
        self.head = n

    def addAtEnd(self, element):
        n = Node(element)
        if self.head is None:
                self.head = n
                return
        last = self.head
        while last.next:
            last = last.next
        last.next = n


def find_middle(linked_list):
    n = len(linked_list)
    middle = linked_list.head
    count = 1
    while count <= n / 2:
        middle = middle.next
        count += 1
    return middle.val


lkd = LinkedList(values=[1, 2, 3, 4, 5])
r = find_middle(lkd)
assert r == 3

lkd = LinkedList(values=[1, 2, 3, 4, 5, 6])
r = find_middle(lkd)
assert r == 4
