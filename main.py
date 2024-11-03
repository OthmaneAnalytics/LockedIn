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


class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return temp

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val= val
            return
        if self.val > val: 
            if self.left is None:
                self.left = BSTNode(val)
                return
            else:
                self.left.insert(val)
                return
        else: 
            if self.right is None:
                self.right = BSTNode(val)
                return
            else:
                self.right.insert(val)
                return

    def get_min(self):
        if not self.val:
            return None
        index = self
        while index.left:
            index = index.left
        return index.val
            

    def get_max(self):
        if not self.val:
            return None
        index = self
        while index.right:
            index = index.right
        return index.val
    
    def delete(self, val):
        if  not self.val:
            return 
        elif self.val > val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        elif self.val < val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        else:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            else:
                node = self.right
                while node.left:
                    node = node.left
                self.val = node.val
                node = node.right
                return self
    
    def preorder(self, visited):
        if self.val:
            visited.append(self.val)
            if self.left:
                self.left.preorder(visited)
            if self.right:
                self.right.preorder(visited)
        return visited

import random
       

class User:
    def __init__(self, id):
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        return isinstance(other, User) and self.id > other.id

    def __repr__(self):
        return "".join(self.user_name)


def get_users(num):
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users



