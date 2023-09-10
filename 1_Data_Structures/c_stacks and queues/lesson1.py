# implementation of queue with ll
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False

    def is_empty(self):
        if (self.head is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if (self.is_empty()):
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node.data

    def remove_head(self):
        if (self.is_empty()):
            return False
        nodeToRemove = self.head
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length -= 1
        return nodeToRemove.data

    def tail_node(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False

    def __str__(self):
        val = ""
        if (self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while (temp.next_element):
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def print_list(self):
        return self.items.__str__()


if __name__ == "__main__":
    queue_obj = MyQueue()
    print("queue.enqueue(2);")
    queue_obj.enqueue(2)
    print("queue.enqueue(4);")
    queue_obj.enqueue(4)
    print("queue.enqueue(6);")
    queue_obj.enqueue(6)
    print("queue.enqueue(8);")
    queue_obj.enqueue(8)
    print("queue.enqueue(10);")
    queue_obj.enqueue(10)

    queue_obj.print_list()

    print("is_empty(): " + str(queue_obj.is_empty()))
    print("front(): " + str(queue_obj.front()))
    print("rear(): " + str(queue_obj.rear()))
    print("size(): " + str(queue_obj.size()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("queue.enqueue(12);")
    queue_obj.enqueue(12)
    print("queue.enqueue(14);")
    queue_obj.enqueue(14)

    while queue_obj.is_empty() is False:
        print("Dequeue(): " + str(queue_obj.dequeue()))

    print("is_empty(): " + str(queue_obj.is_empty()))
