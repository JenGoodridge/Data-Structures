class Item():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_item = Item(data)
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            new_item = Item(data)
            self.tail.next = new_item
            self.tail = new_item

    def pop(self):
        if self.head is None:
            return False
        else:
            new_head = self.head.next
            self.head = new_head

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        string = "["
        current = self.head
        while current is not None:
            string += str(current.data)
            current = current.next
            if current is not None:
                string += ","

        return string + "]"
