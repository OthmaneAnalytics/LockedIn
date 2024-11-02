def count_marketers(job_titles):
    count = 0
    for item in job_titles:
        if item == "marketer":
            count += 1
    return count

def last_work_experience(work_experiences):
    if work_experiences == []:
        return None
    else:
        return work_experiences[-1]

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        else:
            return None

    def pop(self):
        if self.size() > 0:
            item = self.peek()
            self.items.pop()
            return item
        else:
            return None

def is_balanced(input_str):
    par_s = Stack()
    for item in input_str:
        print(item)
        if item == ")" and par_s.peek() == "(":
            par_s.pop()
        else:
            par_s.push(item)
    if par_s.size() > 0:
        return False
    else:
        return True


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            item = self.items[0]
            del self.items[0]
            return item
        else:
            return None

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None
        self.teal = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

#    def add_to_tail(self, node):
#        if self.head is None:
#            self.head = node
#        else:
#            last = None
#            index = self.head
#            while index is not None:
#                last = index
#                index = index.next 
#            last.next = node

    def add_to_head(self, node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node 
        


    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

