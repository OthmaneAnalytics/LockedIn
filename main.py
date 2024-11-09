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


    def postorder(self, visited):
        if self.val:
            if self.left:
                self.left.postorder(visited)
            if self.right:
                self.right.postorder(visited)
            visited.append(self.val)
        return visited

    def inorder(self, visited):
        if self.val:
            if self.left:
                self.left.inorder(visited)
            visited.append(self.val)
            if self.right:
                self.right.inorder(visited)
        return visited

    def exists(self, val):
        if not self.val:
            return False
        if self.val == val:
            return True
        else:
            exist = False
            if self.right:
                exist = exist or self.right.exists(val)
            if self.left:
                exist = exist or self.left.exists(val)
            return exist

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

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil



    def insert(self, val):
        node = RBNode(val)
        node.left = self.nil
        node.right = self.nil
        node.red = True
        node.parent = None
        
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if node.val < current.val:
                current = current.left
            elif node.val > current.val:
                current = current.right
            else:
                return

        node.parent = parent
        if parent is None:
            self.root = node
        else:
            if node.parent.val < node.val:
                parent.right = node
            else:
                parent.left = node
        self.fix_insert(node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent
            if parent == grandparent.right:
                uncle = grandparent.left
                
                if uncle.red:
                    uncle.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    
                    if new_node == new_node.parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(pivot_parent)
            elif parent == grantdparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == new_node.parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False
        

        

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
        
    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

class HashMap:
    def key_to_index(self, key):
        index = 0
        for i in range(len(key)):
            index += ord(key[i])
        index %= len(self.hashmap)
        return index

    def get(self, key):
        index = self.key_to_index(key)
        if self.hashmap[index]:
            return self.hashmap[index][1]
        else:
            raise Exception("sorry, key not found")
    # don't touch below this line

    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key,value)
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

class Trie:
    def add(self, word):
        current = self.root
        for item in word:
            if not item in current.keys():
                current[item] = {}
            current = current[item]
        current[self.end_symbol] = True

    def exists(self, word):
        current = self.root
        for item in word:
            if not item in current.keys():
                return False
            else:
                current = current[item]
        if self.end_symbol in current:
            return True
        else:
            return False

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur.keys():
            words += cur_prefix
        letters = cur.keys()
        for letter in sorted(letters):
            if self.end_symbol != letter:
                words += self.search_level( cur[letter],cur_prefix + letter, words)
        return words

    def words_with_prefix(self, prefix):
        words = []
        content = self.root
        for letter in prefix:
            if letter in content.keys():
                content = content[letter]
            else:
                return []
        return self.search_level(content,prefix,words)

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for i in range(num_vertices):
            self.graph.append([False for item in range(num_vertices)])
            print(self.graph)


    def add_edge(self, u, v):
        print("u ", u , " v ", v)
        self.graph[u][v], self.graph[v][u] = True , True


    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

