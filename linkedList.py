import unittest


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            self.head = Node(data, self.head)

    def deleteNode(self, data):
        current = self.head
        while current.next is not None and current.data is not data:
            previous = current
            current = current.next

        if current.next is None and current.data is not data:
            return False

        elif current.data == self.head.data:
            self.head = self.head.next

        else:
            previous.next = current.next

    def __str__(self):
        string = "["
        current = self.head
        while current:
            string += str(current.data)
            current = current.next
            if current:
                        string += ","

        return string + "]"


class TestlinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.list = linkedList()
        self.list.prepend(0)
        self.list.append(1)
        self.list.append(2)
        self.list.prepend(-1)

    def test_append_prepend(self):
        self.assertEqual(self.list.head.data, -1)
        self.assertEqual(self.list.head.next.data, 0)

    def test_deleteNode(self):
        self.assertEqual(self.list.deleteNode(1), None)
        self.assertEqual(self.list.head.next.next.data, 2)

    def test_deleteNode_differentOrder(self):
        self.assertEqual(self.list.deleteNode(0), None)
        self.assertEqual(self.list.head.next.data, 1)


if __name__ == '__main__':
    unittest.main()
