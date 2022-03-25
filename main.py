

class Stack:

    def __init__(self):
        self.list = []

    def isempty(self):
        if not self.list:
            return False
        else:
            return True

    def push(self, new_element):
        self.list.append(new_element)

    def pop(self):
        self.list.pop()
        return self.list[-1]

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


def balance(bracket_list):
    if len(bracket_list) % 2 != 0:
        print('Несбалансировано')
    else:

