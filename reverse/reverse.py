class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print_nodes(self):
        print('\n')
        current = self.head
        if current is not None:
            while current.next_node is not None:
                print(f"[ {current.value} ] -> ", end='')
                current = current.next_node
            print(f"[ {current.value} ] -> NONE\n")

    def reverse_list(self, node, prev):
        # Check for empty list
        # Grab the node that is at the end of the list
        # Call reverse_list recursively on that value
        if node is None:
            return
        if node.next_node is None:  # This is the end of the regular list, so it needs to become the head
            self.head = node
            return node
        self.reverse_list(node.next_node, None)
        node.next_node.next_node = node
        node.next_node = None
