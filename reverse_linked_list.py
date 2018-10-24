'''
Given pointer to the head node of a linked list, the task is to reverse the linked list.
'''

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, *args, **kwargs):
        values = kwargs.get('values', None)
        if values:
            N = len(values)
            for i in range(N):
                j = N - i - 1
                if i == 0:
                    n = Node(values[j])
                else:
                    n = Node(values[j], n)
            self.head = n
        else: self.head = Node()

    def __len__(self):
        h = self.head
        count = 0
        while h :
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


def reverse(linked_list):
    e = linked_list.head
    v = e.val
    rev = LinkedList(values=[v])
    while e.next:
        e = e.next
        v = e.val
        rev.addAtBeginning(v)
    return rev

lkd = LinkedList(values=[1, 2, 3, 4, 5, 6, 7])
r = reverse(lkd)
print(r)
