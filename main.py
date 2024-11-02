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



